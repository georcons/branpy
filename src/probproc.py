def tokenizer(problem_statement):
    problem_statement = problem_statement.lower()
    invalid_chars = [',', '.', '?', '!', '(', ')', '>', '<', ';', '%', ":", "+", "-", "$", '{', "|", "}", "*", "^", "\\", "/" ,"_", 
    "=", "[", "]", "~"] #, "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_invalid_chars = len(invalid_chars)
    for i in range(num_invalid_chars):
        problem_statement = problem_statement.replace(invalid_chars[i], ' ')
    arr = problem_statement.split()
    return ' '.join(arr)


def load_problems(problems):
    output = []
    length = len(problems)
    for i in range(length):
        new = tokenizer(problems[i])
        output.append(new)
    return output