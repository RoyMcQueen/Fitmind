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

thought_entries_df = pd.DataFrame(columns = ['Thoughts','Sent_Negative','Sent_Neutral','Sent_Positive',
                                                'Sentiment'])


def thought_entry_specialist(thought):
    
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

    

    return [thought,scores[0],scores[1],scores[2], max(zipped)[1]]#,timestamp.strftime("%B %d, %Y, %H:%Mh")]



def spec_apply(row):
    
    timestamp = datetime.datetime.now()

    encoded_thought = tokenizer(row['Thought'], return_tensors='pt')

    output = model(**encoded_thought)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    for i in range(len(scores)):
    
        l = labels[i]
        s = scores[i]

    
    scores_list = [scores[i] for i in range(len(scores))]
    labels_list = [labels[i] for i in range(len(scores))]
    zipped = list(zip(scores_list,labels_list))

    

    return [scores[0],scores[1],scores[2]]#,timestamp.strftime("%B %d, %Y, %H:%Mh")]