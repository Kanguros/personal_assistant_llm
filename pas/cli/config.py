import os
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from typer import CallbackParam, Context, get_app_dir

from pas.utils.log import logger
from pas.utils.yaml_io import read_yaml_file


APP_NAME = "pas"
APP_DIR = Path(get_app_dir(APP_NAME))

LOG_FILE_NAME = "debug.log"
LOG_FILE_PATH = APP_DIR / LOG_FILE_NAME

CONFIG_ENV_NAME = "PAS_CONFIG_PATH"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_PATH = os.getenv(CONFIG_ENV_NAME, APP_DIR / CONFIG_FILE_NAME)


class AssistantConfig(BaseModel):
    name: str = "Helpful Assistant"
    description: str = "You are a helpful assistant."
    instructions: Optional[list[str]] = None
    model: str = "llama3"
    markdown: bool = True

    model_config = ConfigDict(arbitrary_types_allowed=True)


class Config(BaseModel):
    default_assistant: AssistantConfig = Field(default_factory=AssistantConfig)
    model_config = ConfigDict(arbitrary_types_allowed=True)


def load_config(ctx: Context, param: CallbackParam, value: str):
    if ctx.resilient_parsing:
        return None
    print(f"config value: {value}")
    if CONFIG_PATH.exists():
        logger.debug(f"Loading config from {CONFIG_PATH}")
        file_data = read_yaml_file(CONFIG_PATH)
        return Config(**file_data)
    logger.debug("No config file found. Using default values")
    return Config()
