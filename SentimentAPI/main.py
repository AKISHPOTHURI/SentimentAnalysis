from Sentiment import logger
from Sentiment.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Sentiment.pipeline.stage_02_data_validation import DataIngestionValidationPipeline
from Sentiment.pipeline.stage_03_data_transformation import DataTransformationPipeline
from Sentiment.pipeline.stage_04_model_training import ModelTrainerPipeline
from Sentiment.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
      raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
     logger.exception(e)
     raise e


