import os
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict
from typer import get_app_dir

from pas.utils.log import logger
from pas.utils.yaml_io import read_yaml_file

APP_NAME = "pas"
APP_DIR = Path(get_app_dir(APP_NAME, roaming=False))

LOG_FILE_NAME = "debug.log"
LOG_FILE_PATH = APP_DIR / LOG_FILE_NAME

CONFIG_ENV_NAME = "PAS_CONFIG_PATH"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_DEFAULT_PATH = APP_DIR / CONFIG_FILE_NAME
CONFIG_PATH = os.getenv(CONFIG_ENV_NAME, CONFIG_DEFAULT_PATH)


class Config(BaseModel):
    name: str = "Helpful Assistant"
    description: str = "You are a helpful assistant."
    instructions: Optional[list[str]] = None
    model: str = "llama3"
    markdown: bool = True
    add_storage: bool = True

    file_path: Optional[Path] = None
    dir_path: Optional[Path] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def from_file(cls, file_path: Optional[str] = None) -> "Config":
        logger.debug(f"Loading config from: {file_path}")
        config_kwargs = {}
        if file_path:
            file_path = Path(file_path)
            if file_path.exists():
                config_kwargs = read_yaml_file(file_path)
        else:
            logger.debug(f"No config file found. Using default path: {CONFIG_DEFAULT_PATH}")
            file_path = CONFIG_DEFAULT_PATH
            file_path.parent.mkdir(parents=True, exist_ok=True)
            if file_path.exists():
                config_kwargs = read_yaml_file(file_path)

        return cls(**config_kwargs, file_path=file_path, dir_path=file_path.parent)
