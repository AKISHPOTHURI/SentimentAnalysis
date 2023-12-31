from Sentiment import logger
from Sentiment.components.data_validation import DataValiadtion
from Sentiment.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation Stage"

class DataIngestionValidationPipeline:
    def __init__(self):
         pass
    
    def main(self):
             config = ConfigurationManager()
             data_validation_config = config.get_data_validation_config()
             data_validation = DataValiadtion(config=data_validation_config)
             data_validation.validate_all_files_exist()
    

if __name__ == "__main__":
    try:
          logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
          obj = DataIngestionValidationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
         logger.exception(e)
         raise e
