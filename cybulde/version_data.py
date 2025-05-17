from pathlib import Path  # 'pathlib.Path' imported but unused

from cybulde.config.schemas.config_schema import Config
from cybulde.utils.imports import get_config
from cybulde.utils.data_utils import initialize_dvc
from cybulde.utils.utils import get_logger  # imported but unused

@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:  # "config" is not accessed
    initialize_dvc()

if __name__ == "__main__":
    version_data()  # type: ignore
