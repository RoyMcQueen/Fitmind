from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import datetime
import time
import speech_recognition as sr
import pandas as pd

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']



def thought_entry(thought):

    # thought = input('What is your thought?')

    timestamp = datetime.datetime.now()

    encoded_thought = tokenizer(thought, return_tensors='pt')

    output = model(**encoded_thought)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    for i in range(len(scores)):
    
        l = labels[i]
        s = scores[i]

    
    scores_list = [scores[i] for i in range(len(scores))]
    labels_list = [labels[i] for i in range(len(scores))]
    zipped = list(zip(scores_list,labels_list))


    return max(zipped)[1]