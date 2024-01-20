from sklearn.model_selection import train_test_split
import keras
from Sentiment import logger
from Sentiment.entity.config_entity import ModelTrainerConfig
import pandas as pd 
import os
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from keras.utils import pad_sequences

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def loadData(self):
        sentiData = pd.read_excel(self.config.data_path)
        sentiData.drop('Unnamed: 0',axis=1,inplace=True)
        sentiData.dropna(how="any", inplace=True)
        return sentiData
    
    def convertToLower(self,data):
        '''
        Converting data to the lowercase
        '''
        data.loc[:, 'Review'] = data.loc[:, 'Review'].str.lower()
        logger.info(f"Data converted to lowercase")
        return data

    def splitData(self,sentiData):
        '''
        Splitting the data into train and test.
        '''
        trainSentences, testSentences, trainLabels, testLabels = train_test_split(sentiData['Review'],sentiData['sentiment'] , stratify = sentiData['sentiment'])
        return trainSentences, testSentences, trainLabels, testLabels
    
    def TextToNumeric(self,trainSentences,testSentences):
        '''
        Converting the text to numeric
        '''
        tokenizer = Tokenizer(num_words = self.config.vocab_size, oov_token=self.config.oov_tok)
        tokenizer.fit_on_texts(trainSentences)
        word_index = tokenizer.word_index
        # convert train dataset to sequence and pad sequences
        trainSequences = tokenizer.texts_to_sequences(trainSentences)
        trainPadded = pad_sequences(trainSequences, padding=self.config.padding_type, maxlen=self.config.max_length)
        # convert Test dataset to sequence and pad sequences
        testSequences = tokenizer.texts_to_sequences(testSentences)
        testPadded = pad_sequences(testSequences, padding=self.config.padding_type, maxlen=self.config.max_length)
        return trainPadded,testPadded
    
    def prepareModel(self):
        '''
        model preparation
        '''
        # model initialization
        model = keras.Sequential([
            keras.layers.Embedding(self.config.vocab_size, self.config.embedding_dim, input_length=self.config.max_length),
            keras.layers.Bidirectional(keras.layers.LSTM(units=self.config.units,return_sequences=True)),
            keras.layers.Bidirectional(keras.layers.LSTM(self.config.units)),
            keras.layers.Dense(self.config.dense_layers, activation=self.config.hidden_dense),
            keras.layers.Dense(self.config.last_layer, activation=self.config.last_dense)
        ])
        # compile model
        model.compile(loss=self.config.loss,
                    optimizer=self.config.optimizer,
                    metrics=[self.config.metrics])
        logger.info(model.summary())
        return model
    
    def trainModel(self,model,trainPadded,trainLabels):
            model.fit(trainPadded, trainLabels,epochs=self.config.num_epochs, verbose=self.config.verbose,validation_split=self.config.validation_split)
            return model
    
    def saveModel(self,model) -> bool:
         model.save(os.path.join(self.config.root_dir,"LSTMModel"+"V6"+".h5"))
         model.save(os.path.join(self.config.model_ckpt,"LSTMModel"+"V6"+".h5"))
         return True