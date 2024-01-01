from Sentiment import logger
from Sentiment.components.data_transformation import DataTransformation
from Sentiment.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"

class DataIngestionValidationPipeline:
    def __init__(self):
         pass
    
    def main(self):
             config = ConfigurationManager()
             data_transformation_config = config.get_data_transformation_config()
             data_transformation = DataTransformation(config=data_transformation_config)
             sentiData = data_transformation.load()
             data_transformation
          #    sentiData = data_transformation.shuffle(sentiData)
          #    sentiData['sentiment'] = sentiData['sentiment'].apply(data_transformation.labelling)
          #    sentiData['Review'] = sentiData['Review'].apply(data_transformation.removeStopwords)
          #    sentiData['Review'] = sentiData['Review'].apply(data_transformation.lemmatizeText)

if __name__ == "__main__":
    try:
          logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
          obj = DataIngestionValidationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
         logger.exception(e)
         raise e