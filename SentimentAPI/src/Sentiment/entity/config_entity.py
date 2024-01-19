from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    save_dir: Path
    save_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    vocab_size: int
    oov_tok: str
    embedding_dim: int
    max_length: int # choose based on statistics, for example 150 to 200
    padding_type: str
    trunc_type: str
    units: int #units: The number of hidden units in the layer.
    hidden_dense: str
    last_dense: str
    loss: str
    optimizer: str
    metrics: str
    num_epochs: int
    verbose: int
    validation_split: int
    last_layer: int
    dense_layers: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    METRIC_FILE: Path
    mlflow_uri: str
    all_params: dict
    model: Path