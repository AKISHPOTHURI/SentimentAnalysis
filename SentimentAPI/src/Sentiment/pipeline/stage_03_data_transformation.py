from Sentiment import logger
from Sentiment.components.data_transformation import DataTransformation
from Sentiment.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
         pass
    
    def main(self):
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

if __name__ == "__main__":
    try:
          logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
          obj = DataTransformationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
         logger.exception(e)
         raise e