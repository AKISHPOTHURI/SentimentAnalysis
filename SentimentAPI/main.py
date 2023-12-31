from Sentiment import logger
from Sentiment.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Sentiment.pipeline.stage_02_data_validation import DataIngestionValidationPipeline


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionValidationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
         logger.exception(e)
         raise e