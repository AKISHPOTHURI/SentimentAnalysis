from Sentiment.constants import *
import string,time
import os
from nltk.corpus import stopwords
from Sentiment import logger
import nltk
import emoji
from textblob import TextBlob
from datasets import load_dataset, load_from_disk
import pandas as pd
import sklearn
from Sentiment.entity.config_entity import DataTransformationConfig
nltk.download('stopwords')
nltk.download('wordnet')

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def removePuntuations(self,text):
        punctuation = string.punctuation
        return text.translate(str.maketrans('', '', punctuation))

    def removeStopwords(self,text):
        newText = []

        for word in text.split():
            if word in stopwords.words('english'):
                newText.append('')
            else:
                newText.append(word)
        x = newText[:]
        newText.clear()
        return " ".join(x)


    def lemmatizeText(self,text):
        w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
        lemmatizer = nltk.stem.WordNetLemmatizer()
        sentence = ""
        for word in w_tokenizer.tokenize(text):
            sentence = sentence + lemmatizer.lemmatize(word) + " "
        return sentence

    def chatConversion(self,text):
        newText = []
        for word in text.split():
            if word.upper() in chatWords:
                newText.append(chatWords[word.upper()])
            else:
                newText.append(word)
        return " ".join(newText)

    def decodeEmoji(self,text):
        return emoji.demojize(text).replace(":",'').replace("_"," ")

    def correctText(self,text):
        return TextBlob(text).correct().string

    def labelling(self,sentiment):
        if sentiment == 'positive':
            return 1
        elif sentiment == 'negative':
            return 0
        elif sentiment == 1:
            return 1
        elif sentiment == 0:
            return 0
        return True

    def shuffle(self,sentiData):
        for i in range(50):
            sentiData = sklearn.utils.shuffle(sentiData)
        return sentiData

    def load(self):
        sentiData = pd.read_excel(self.config.data_path)
        return sentiData
    
    def saveToExcel(self,sentiData):
            return sentiData.to_excel(os.path.join(self.config.save_path))