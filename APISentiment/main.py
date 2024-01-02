import os
import sys 
# sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
sys.path.insert(0, './src')
from src.app.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.app.utils.common import logger 


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


