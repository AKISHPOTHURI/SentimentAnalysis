import os
from Sentiment import logger
import keras
from sklearn import metrics
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from Sentiment.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def loadModel(self):
        '''
        Model Loading from the artifacts
        '''
        model = keras.models.load_model(os.path.join(self.config.model,"LSTMModel"+"V2"+".h5"))
        return model
    
    def predictTest(self,testSentences,model):
        '''
        test Sentence prediction
        '''
        return model.predict(testSentences)
    
    def sentimentClassify(self,predictions):
        prediction = []
        for i in predictions:
            if i > 50:
                prediction.append(1)
            else:
                prediction.append(0)
        return prediction
    
    def TextToNumeric(self,testSentences):
        '''
        Converting the text to numeric
        '''
        try:
            vocab_size = 3000 # choose based on statistics
            oov_tok = ''
            max_length = 200
            padding_type = 'post'
            tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
            tokenizer.fit_on_texts(testSentences)
            word_index = tokenizer.word_index
            # convert Test dataset to sequence and pad sequences
            testSequences = tokenizer.texts_to_sequences(testSentences)
            testPadded = pad_sequences(testSequences, padding=padding_type, maxlen=max_length)
            return testPadded
        except Exception as e:
            raise e
    
    def EvaluationMetrics(self,predictions,testLabels):
        '''
        Finding evaluation metrics
        '''
        try:
            accuracyScore = metrics.accuracy_score(testLabels,predictions,average='weighted',zero_division=0)
            recallScore = metrics.recall_score(testLabels,predictions,average='weighted',zero_division=0)
            precisionScore = metrics.precision_score(testLabels,predictions,average='weighted',zero_division=0)
            f1Score = metrics.f1_score(testLabels,predictions,average='weighted',zero_division=0)
            return accuracyScore,recallScore,precisionScore,f1Score
        except Exception as e:
            raise e
        
    def ModelEvaluationStatus(self,accuracyScore,recallScore,precisionScore,f1Score) -> bool:
        '''
        storing the metrics results in a text file
        '''
        try:
            Evaluation_status = None

            all_files = os.listdir(os.path.join("artifacts","model_evaluation"))
    
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    Evaluation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Evaluation status: {Evaluation_status}")
                else:
                    Evaluation_status = True
                    
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Evaluation status: {Evaluation_status}"+",")
                        f.write(f"accuracyScore: {accuracyScore}"+",")
                        f.write(f"recallScore: {recallScore}"+",")
                        f.write(f"precisionScore: {precisionScore}"+",")
                        f.write(f"f1Score: {f1Score}"+",")

            return Evaluation_status
        
        except Exception as e:
            raise e