from Sentiment.config.configuration import ConfigurationManager
from Sentiment.components.model_trainer import ModelTrainer
from Sentiment.components.model_evaluation import ModelEvaluation
from Sentiment import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
         pass
    
    def main(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            logger.info(f"data loading Started")
            sentiData = model_trainer_config.loadData()
            logger.info(f"data loading Completed")
            logger.info(f"data Lowercase convertion Started")
            sentiData = model_trainer_config.convertToLower(sentiData)
            logger.info(f"data Lowercase convertion Completed")
            logger.info(f"data Splitting Started")
            trainSentences, testSentences, trainLabels, testLabels = model_trainer_config.splitData(sentiData)
            logger.info(f"data Splitting Completed")
            logger.info(f"tokenizing the Text Started")
            testPadded = model_evaluation_config.TextToNumeric(testSentences)
            logger.info(f"tokenizing the Text Completed")
            logger.info(f"Model Loading")
            model = model_evaluation_config.loadModel()
            logger.info(f"Model Loaded")
            logger.info(f"Predicting Test Data")
            predictions = model_evaluation_config.predictTest(testPadded,model)
            logger.info(f"Predicting Test Data Completed")
            logger.info(f"Predicting classification Started")
            prediction = model_evaluation_config.sentimentClassify(predictions)
            logger.info(f"Predicting classification Completed")
            logger.info(f"EvaluationMetrics Started")
            accuracyScore = model_evaluation_config.EvaluationMetrics(prediction,testLabels)
            logger.info(f"EvaluationMetrics Completed")
            logger.info(f"Updating MLFLOW started")
            model_evaluation_config.log_into_mlflow(accuracyScore,model)
            logger.info(f"Updating MLFLOW Completed")
            model_evaluation_config.ModelEvaluationStatus(accuracyScore)
            logger.info(f"EvaluationMetrics Saved")

if __name__ == "__main__":
    try:
          logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
          obj = ModelEvaluationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
         logger.exception(e)
         raise e