import os
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from typer import CallbackParam, Context, get_app_dir

from pas.utils.log import logger, set_log_level_to_debug
from pas.utils.yaml_io import read_yaml_file

if TYPE_CHECKING:
    pass

APP_NAME = "pas"
APP_DIR = Path(get_app_dir(APP_NAME))

LOG_FILE_NAME = "debug.log"
LOF_PATH = APP_DIR / LOG_FILE_NAME

CONFIG_ENV_NAME = "PAS_CONFIG_PATH"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_PATH = os.getenv(CONFIG_ENV_NAME, APP_DIR / CONFIG_FILE_NAME)


class Config(BaseModel):
    default_model: str = "llama3"

    model_config = ConfigDict(arbitrary_types_allowed=True)


def load_config(ctx: Context, param: CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    if CONFIG_PATH.exists():
        logger.debug(f"Loading config from {CONFIG_PATH}")
        file_data = read_yaml_file(CONFIG_PATH)
        return Config(**file_data)
    logger.debug("No config file found. Using default values")
    return Config()


def set_debug(ctx: Context, param: CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    if not value:
        return
    return set_log_level_to_debug("DEBUG")


class Panel(str, Enum):
    OPTIONS = "Options"
