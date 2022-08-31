# loading in all the essentials for data manipulation
import pandas as pd
import numpy as np

#load in the NTLK stopwords to remove articles, preposition and other words that are not actionable
from nltk.corpus import stopwords

# This allows to create individual objects from a bog of words
from nltk.tokenize import word_tokenize

# Lemmatizer helps to reduce words to the base form

from nltk.stem import WordNetLemmatizer

# Ngrams allows to group words in common pairs or trigrams..etc
from nltk import ngrams

# We can use counter to count the objects from collections
from collections import Counter

# This is our visual library
import seaborn as sns
import matplotlib.pyplot as plt




def word_frequency(text):

    # joins all the sentenses
    # sentence ="".join(sentence)

    # creates tokens, creates lower class, removes numbers etc

    # text = dataframe['Thoughts'].str.cat(sep = ' ') ## add this line into the mix so it conca

    

    new_tokens = word_tokenize(text)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens =[t for t in new_tokens if t not in stopwords.words('english')]
    new_tokens = [t for t in new_tokens if t.isalpha()]
    lemmatizer = WordNetLemmatizer()
    new_tokens =[lemmatizer.lemmatize(t) for t in new_tokens]

    #counts the words, pairs and trigrams
    counted = Counter(new_tokens)
    counted_2= Counter(ngrams(new_tokens,2))
    counted_3= Counter(ngrams(new_tokens,3))

    #creates 3 data frames and returns them
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
    trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)

    word_freq['word_freq'] = (word_freq['word'] + ' ') * word_freq['frequency']
    
    return word_freq # word_pairs,trigrams



def word_frequency_pairs(text):

    # joins all the sentenses
    # sentence ="".join(sentence)

    # creates tokens, creates lower class, removes numbers etc

    # text = dataframe['Thoughts'].str.cat(sep = ' ') ## add this line into the mix so it conca

    

    new_tokens = word_tokenize(text)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens =[t for t in new_tokens if t not in stopwords.words('english')]
    new_tokens = [t for t in new_tokens if t.isalpha()]
    lemmatizer = WordNetLemmatizer()
    new_tokens =[lemmatizer.lemmatize(t) for t in new_tokens]

    #counts the words, pairs and trigrams
    counted = Counter(new_tokens)
    counted_2= Counter(ngrams(new_tokens,2))
    counted_3= Counter(ngrams(new_tokens,3))

    #creates 3 data frames and returns them
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
    trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)

    word_freq['word_freq'] = (word_freq['word'] + ' ') * word_freq['frequency']
    
    return word_pairs