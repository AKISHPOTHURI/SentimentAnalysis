from Sentiment.constants import *
from Sentiment.utils.common import read_yaml, create_directories
from Sentiment.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from Sentiment import logger

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_present_dir,
            data_path=config.data_present_path,
            save_dir=config.root_dir,
            save_path=config.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,
            vocab_size = params.vocab_size,
            oov_tok = params.oov_tok,
            embedding_dim = params.embedding_dim,
            max_length = params.max_length, # choose based on statistics, for example 150 to 200
            padding_type =  params.padding_type,
            trunc_type = params.trunc_type,
            units = params.units, #units: The number of hidden units in the layer.
            hidden_dense = params.hidden_dense,
            last_dense = params.last_dense,
            loss = params.loss,
            optimizer = params.optimizer,
            metrics = params.metrics,
            num_epochs = params.num_epochs,
            verbose = params.verbose,
            validation_split = params.validation_split,
            dense_layers = params.dense_layers,
            last_layer = params.last_layer
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            METRIC_FILE = config.METRIC_FILE,
            model = config.model,
        )

        return model_evaluation_config