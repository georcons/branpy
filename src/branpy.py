import openai
import pickle
import json
import string
import random
from operator import itemgetter
from prompts import FILTER_SYSTEM_PROMPT
from prompts import GENERATE_USER_PROMPT
from tasks import map_main_task
from tasks import map_reduced_to_main
from tasks import map_reduced_task
from probproc import load_problems

class DomainClfBatchRetriever:
    def __init__(self, batch_id):
        self.batch_id = batch_id
        self.apikeyset = False

    def SetOpenAiApiKey(self, key):
        openai.api_key = key
        self.apikeyset = True

    def retrieve(self):
        res = openai.batches.retrieve(self.batch_id)

        if (res.status != "completed"):
            return {"status": res.status}

        output_file_id = res.output_file_id
        output_file = openai.files.content(output_file_id).text
        output_lines = output_file.splitlines()

        output_list = []

        if len(output_lines) == 0:
            return []

        id_init = json.loads(output_lines[0].strip())['custom_id']
        blocks_init = id_init.split("-")

        if len(blocks_init) != 3:
            return []

        total_count = int(blocks_init[1])

        for i in range(total_count):
            output_list.append("")

        for line in output_lines:
            obj = json.loads(line.strip())
            blocks = obj['custom_id'].split("-")

            if len(blocks) == 3:
                current_task = blocks[2]
                current_index = int(blocks[0])
                result = obj['response']['body']['choices'][0]['message']['content']

                if current_task == "main":
                    result = map_main_task(result)
                if current_task == "reduced":
                    result = map_reduced_task(result)
                
                output_list[current_index] = result

        return {"status": "completed", "result": output_list}


class DomainClf:

    def __init__(self, method="openai", task="main", model="gpt-4o-mini", directory="./"):
        if method == "openai" or method == "openai-batch" or method == "offline":
            self.method = method

        if method == "openai" or method == "openai-batch":
            if self.is_model_valid(model):
                self.model = model
            else:
                raise Exception("Unsupported model. Use gpt-4o-mini or gpt-4o.")

        if self.is_task_valid(task):
            self.task = task
        else:
            raise Exception("Invalid task.")

        self.directory = directory
        self.apikeyset = False



    def is_task_valid(self, task):
        return task == "main" or task == "reduced" or task == "complete"



    def SetOpenAiApiKey(self, key):
        openai.api_key = key
        self.apikeyset = True
        


    def is_model_valid(self, m):
        return m == "gpt-4o-mini" or m == "gpt-4o"




    def score(self, statements, groundtruths, groundtruths_type="main"):
        if (groundtruths_type == "reduced" and self.task =="complete") or (groundtruths_type == "main" and self.task != "main"):
            raise Exception("Ground-truths type must be of level lower or equal to the task type level.")

        if self.method == "openai-batch":
            raise Exception("Score is not supported with openai-batch.")

        y_hat = self.classify(statements)
        count = 0
        index = 0

        for prediction in y_hat:
            y_gt = groundtruths[index]

            if groundtruths_type == "complete" and self.task == "main":
                y_gt = map_main_task(y_gt)

            if groundtruths_type == "reduced" and self.task == "main":
                y_gt = map_reduced_to_main(y_yg)

            if groundtruths_type == "complete" and self.task == "reduced":
                y_gt = map_reduced_task(y_gt)

            if (prediction == y_gt):
                count += 1
            index += 1

        return count / index
        



    def classify(self, statements):
        if isinstance(statements, str):
            return self.classify(self, [statements])
        
        if not isinstance(statements, list):
            return []

        if self.method == "openai":
            return self._classify_openai(statements)

        if self.method == "openai-batch":
            return self._create_openai_batch(statements)

        if self.method == "offline":
            return self._classify_bayesian(statements)

        raise Exception("Invalid Classifier method.")



    def _classify_openai(self, statements):
        if not self.apikeyset:
            raise Exception("OpenAI API Key not set. Use .SetOpenAiApiKey(your_key).")

        output = []
        model = self.model
        
        system_prompt = FILTER_SYSTEM_PROMPT(filter="none")

        if not self.is_model_valid(model):
            raise Exception("Unsupported model. Use gpt-4o-mini or gpt-4o.")

        else:
            for statement in statements:
                result = self._execute_single_openai_task(statement, model, system_prompt=system_prompt)

                if self.task == "main":
                    result = map_main_task(result)

                if self.task == "reduced":
                    result = map_reduced_task(result)

                output.append(result)
        
        return output
            

    def _create_openai_batch(self, statements):
        tasks = []
        index = 0
        total_count = len(statements)

        for statement in statements:
            tasks.append(self._format_single_task_json(statement, index, total_count))
            index += 1

        filename = self.directory + "file-" + (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(24))) + ".jsonl"

        file = open(filename, "w")

        for obj in tasks:
            file.write(json.dumps(obj) + "\n")

        file.close()

        batch_file = openai.files.create(
            file=open(filename, "rb"),
            purpose="batch"
        )

        batch_job = openai.batches.create(
            input_file_id=batch_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h"
        )

        return batch_job.id


    def _classify_bayesian(self, statements):
        output = []

        if self.task != "complete":
            with open("bayesian.pk", "rb") as file:
                bayes = pickle.load(file)
                vectorizer = bayes["vectorizer"]
                clf = bayes["model"]
                statements = load_problems(statements)
                statements_vectorized = vectorizer.transform(statements)
                results = clf.predict(statements_vectorized)
                if self.task == "main":
                    for result in results:
                        output.append(map_reduced_to_main(result))
                else:
                    output = results
        
        else:
            with open("bayesian-complete.pk", "rb") as file:
                bayes = pickle.load(file)
                vectorizer = bayes["vectorizer"]
                clf = bayes["model"]
                statements = load_problems(statements)
                statements_vectorized = vectorizer.transform(statements)
                results = clf.predict(statements_vectorized)
                output = results

        return output
                    
    def _format_single_task_json(self, statement, index, total_count):
        return {
            "custom_id": f"{index}-{total_count}-{self.task}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4o-mini",
                "temperature": 0.7,
                "messages": [
                    {
                        "role": "system",
                        "content": FILTER_SYSTEM_PROMPT("none")
                    },
                    {
                        "role": "user",
                        "content": GENERATE_USER_PROMPT(statement)
                    }
                ],
                "max_tokens": 150
            }
        }
    
    def _execute_single_openai_task(self, statement, model, system_prompt):
        try:
            response = openai.ChatCompletion.create(
                model=model, 
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": GENERATE_USER_PROMPT(statement)}
                ],
                max_tokens=200,
                temperature=0.7 
            )
        
            assistant_response = response['choices'][0]['message']['content'].strip()
            return assistant_response

        except Exception as e:
            raise Exception(f"OpenAI error: {str(e)}")