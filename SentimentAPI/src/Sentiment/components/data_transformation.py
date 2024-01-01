from Sentiment.constants import *
import string,time
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

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def removePuntuations(self,text):
        punctuation = string.punctuation
        logger.info(f"Sentence removePuntuations")
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
        logger.info(f"Sentence removeStopwords")
        return " ".join(x)


    def lemmatizeText(self,text):
        w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
        lemmatizer = nltk.stem.WordNetLemmatizer()
        sentence = ""
        for word in w_tokenizer.tokenize(text):
            sentence = sentence + lemmatizer.lemmatize(word) + " "
        logger.info(f"Sentence lemmatizeText")
        return sentence

    def chatConversion(self,text):
        newText = []
        for word in text.split():
            if word.upper() in chatWords:
                newText.append(chatWords[word.upper()])
            else:
                newText.append(word)
        logger.info(f"Sentence chatConversion")
        return " ".join(newText)

    def decodeEmoji(self,text):
        logger.info(f"Sentence decodeEmoji")
        return emoji.demojize(text).replace(":",'').replace("_"," ")

    def correctText(self,text):
        logger.info(f"Sentence correction")
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
        logger.info(f"Data shuffled")
        return True

    def shuffle(self,sentiData):
        for i in range(50):
            sentiData = sklearn.utils.shuffle(sentiData)
        logger.info(f"Data shuffled")
        return sentiData

    def load(self):
        sentiData = pd.read_excel(self.config.data_path)
        logger.info(f"Data loaded")
        return sentiData