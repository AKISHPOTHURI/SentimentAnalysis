from Sentiment import logger
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