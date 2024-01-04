import os
from Sentiment import logger
import keras
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score

from Sentiment.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def loadModel(self):
        '''
        Model Loading from the artifacts
        '''
        model = keras.models.load_model(os.path.join(self.config.model,"LSTMModel"+"V1"+".h5"))
        return model
    
    def predictTest(self,testSentences,model):
        '''
        test Sentence prediction
        '''
        return model.predict(testSentences)
    
    def EvaluationMetrics(self,predictions,testLabels):
        '''
        Finding evaluation metrics
        '''
        try:
            accuracyScore = accuracy_score(testLabels,predictions)
            recallScore = recall_score(testLabels,predictions)
            precisionScore = precision_score(testLabels,predictions)
            f1Score = f1_score(testLabels,predictions)
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