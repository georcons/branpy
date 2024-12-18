BranPy
======================

This is a python package providing several methods for classifying mathematical problems into domains.


The main class of the package is the ``DomainClf`` class. There are several classification methods.


Possible Tasks
---
At the ``DomainClf`` constructor one can specify to what depth the classifier should make its predictions. To do so 
select ``task='main'`` for the five main branches (Algebra, Geometry, Number Theory, Combinatorics and Others), ``task='reduced'`` to 
predict 24 greater branches and ``task='complete'`` to predict one of all the 139 possible domains in the classifier.



Naive Bayes Classifier
----

To use a pre-trained Naive Bayes Classifier one must specify ``method='offline'`` at the ``DomainClf`` constructor:

    from branpy import DomainClf

    clf = DomainClf(method='offline', task='main')

To classify a list of string problem statements one must call the ``classify()`` method of the created object.

    domains = clf.classify(lst)




GPT Approach
----

Another method for classification is to use an OpenAI model. Specify ``method='openai'`` at the constructor.
To use this method one must first import thair OpenAI API key via the ``SetOpenAiApiKey()`` method.

    from branpy import DomainClf

    clf = DomainClf(method='openai', task='main', model='gpt-4o-mini')
    
    clf.SetOpenAiApiKey("{YOUR_API_KEY}")

    domains = clf.classify(lst)

As of now, only ``gpt-4o-mini`` and ``gpt-4o`` models are supported.




OpenAI Batch API
----

To reduce costs one may use the Batch API of OpenAI. Specify ``method=='openai-batch'``. 
Once again the use has to set thei OpenAI API key. In this case the ``classify()`` method return only 
the Batch ID that can be later used to retrieve the result. It is also possible to specify the directory 
at which the batch file will be created. To do that use ``directory={DIRECTORY}`` at the constructor.

    from branpy import DomainClf

    clf = DomainClf(method='openai-batch', task='main', model='gpt-4o-mini')
    
    clf.SetOpenAiApiKey("{YOUR_API_KEY}")

    batch_id = clf.classify(lst)




Retrieving an OpenAI Batch API Request
-----

For batch result retrival the ``DomainClfBatchRetriever`` class is provided. In the contructor put the Batch ID
and use the ``retrieve()`` method to get the results. The method outputs a list of the same length as the number of 
problems requested for classification. At each respective possition the predicted class is set if the result is successful.

    from branpy import DomainClfBatchRetriever

    rtv = DomainClfBatchRetriever(batch_id="{BATCH_ID}")
    
    rtv.SetOpenAiApiKey("{YOUR_API_KEY}")

    result = rtv.retrieve()

The ``retrieve()`` method return a dictionary with a key ``status`` that is ``completed`` if the batch job is done. In this case 
the dicitonary contains a key ``result`` that is a list of the classes.
