from pathlib import Path  # 'pathlib.Path' imported but unused

from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.data_utils import initialize_dvc, initialize_dvc_storage
from cybulde.utils.utils import get_logger  # imported but unused

@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:  # "config" is not accessed
    initialize_dvc()

    initialize_dvc_storage(config.dvc_remote_name, config.dvc_remote_url)

if __name__ == "__main__":
    version_data()  # type: ignore
