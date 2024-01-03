from Sentiment import logger
from Sentiment.components.data_transformation import DataTransformation
from Sentiment.config.configuration import ConfigurationManager
from Sentiment.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Sentiment.pipeline.stage_02_data_validation import DataIngestionValidationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionValidationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
         logger.exception(e)
         raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    config = ConfigurationManager()
    data_transformation_config = config.get_data_transformation_config()
    data_transformation = DataTransformation(config=data_transformation_config)
    logger.info(f"Data Loading Started")
    sentiData = data_transformation.load()
    logger.info(f"Data Loading Ended")
    logger.info(f"Data Shuffling Started")
    sentiData = data_transformation.shuffle(sentiData)
    logger.info(f"Data Shuffling Ended")
    logger.info(f"Data Labelling Started")
    sentiData['sentiment'] = sentiData['sentiment'].apply(data_transformation.labelling)
    logger.info(f"Data Labelling Ended")
    logger.info(f"Data Removing Stopwords Started")
    sentiData['Review'] = sentiData['Review'].apply(data_transformation.removeStopwords)
    logger.info(f"Data Removing Stopwords Ended")
    logger.info(f"Data Lemmatization Started")
    sentiData['Review'] = sentiData['Review'].apply(data_transformation.lemmatizeText)
    logger.info(f"Data Lemmatization Ended")
    logger.info(f"Data Saving Started")
    data_transformation.saveToExcel(sentiData)
    logger.info(f"Data Saving Ended")
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
      logger.exception(e)
      raise e
