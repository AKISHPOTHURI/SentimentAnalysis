import os
from Sentiment import logger
from urllib.parse import urlparse
import mlflow.keras
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
        model = keras.models.load_model(os.path.join(self.config.model,"LSTMModel"+"V6"+".h5"))
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
        
    def log_into_mlflow(self,accuracy,model):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"accuracy": accuracy}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(model,"model",registered_model_name="LSTMModel")
            else:

                mlflow.keras.log_model(model,"model")
    
    def EvaluationMetrics(self,predictions,testLabels):
        '''
        Finding evaluation metrics
        '''
        try:
            accuracyScore = metrics.accuracy_score(testLabels,predictions)
            return accuracyScore
        except Exception as e:
            raise e
            
    def ModelEvaluationStatus(self,accuracyScore) -> bool:
        '''
        storing the metrics results in a text file
        '''
        try:
            Evaluation_status = None

            # all_files = os.listdir(os.path.join("artifacts","model_evaluation"))
            # print(all_files)
            # for file in all_files:
            if accuracyScore == None:
                Evaluation_status = False
                with open(self.config.METRIC_FILE, 'w') as f:
                    f.write(f"Evaluation status: {Evaluation_status}")
            else:
                Evaluation_status = True
                
                with open(self.config.METRIC_FILE, 'w') as f:
                    f.write(f"Evaluation status: {Evaluation_status}"+",")
                    f.write(f"accuracyScore: {accuracyScore}"+",")
            return Evaluation_status
        
        except Exception as e:
            raise e