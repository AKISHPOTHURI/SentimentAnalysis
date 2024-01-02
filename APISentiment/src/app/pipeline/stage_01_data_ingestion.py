import os
import sys 
# sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
sys.path.insert(0, '../src')
from app.config.configuration import ConfigurationManager
from app.components.data_ingestion import DataIngestion
from app.utils.common import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
         pass
    def main(self):
         config = ConfigurationManager()
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion = DataIngestion(config=data_ingestion_config)
         data_ingestion.download_file()
         data_ingestion.extract_zip_file()




if __name__ == '__main__':
     try:
          logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<")
          obj = DataIngestionTrainingPipeline()
          obj.main()
          logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
     except Exception as e:
        logger.exception(e)
        raise e

