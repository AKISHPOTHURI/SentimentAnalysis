from Sentiment.config.configuration import ConfigurationManager
from Sentiment.components.model_trainer import ModelTrainer
from Sentiment import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
         pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        logger.info(f"data loading Started")
        sentiData = model_trainer_config.loadData()
        logger.info(f"data loading Completed")
        logger.info(f"data Lowercase convertion Started")
        sentiData = model_trainer_config.convertToLower(sentiData)
        logger.info(f"data Lowercase convertion Completed")
        logger.info(f"data Splitting Started")
        trainSentences, testSentences, trainLabels, testLabels = model_trainer_config.splitData(sentiData)
        logger.info(f"data Splitting Completed")
        logger.info(f"data TextToNumeric Started")
        trainPadded,testPadded = model_trainer_config.TextToNumeric(trainSentences,testSentences)
        logger.info(f"data TextToNumeric Completed")
        logger.info(f"data prepareModel Started")
        modelArchitectute = model_trainer_config.prepareModel()
        logger.info(f"data prepareModel Completed")
        logger.info(f"data Model Training Started")
        trainedModel = model_trainer_config.trainModel(modelArchitectute,trainPadded,trainLabels)
        logger.info(f"data Model Training Completed")
        model_trainer_config.saveModel(trainedModel)
        logger.info(f"model saved successfully")

if __name__ == "__main__":
    try:
          logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
          obj = ModelTrainerPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
         logger.exception(e)
         raise e