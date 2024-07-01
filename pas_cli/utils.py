from enum import Enum
from pathlib import Path
from typing import Optional

from click import UsageError

from .config import Config
from typer import CallbackParam, Context

from pas.assistant import Assistant
from pas.llm.ollama import Ollama
from pas.storage.sqllite import SqlAssistantStorage
from pas.utils.log import logger, set_log_level_to_debug


class Panel(str, Enum):
    OPTIONS = "Options"
    OUTPUT = "Output Options"


def load_config(ctx: Context, param: CallbackParam, value: str) -> Optional[Config]:
    if ctx.resilient_parsing:
        return None
    return Config.from_file(value)


def set_log_level(ctx: Context, param: CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    if not value:
        return
    if param.name == "verbose":
        set_log_level_to_debug("DEBUG")
    elif param.name == "quiet":
        set_log_level_to_debug("ERROR")
    return


def find_assistant(name: str):
    package_dir = Path(__file__).parent
    assistants_dir = package_dir / "assistant"
    for file_path in assistants_dir.glob("*.yaml"):
        if name in file_path.stem:
            return file_path
    raise UsageError(f"Assistant config file {name} not found in {assistants_dir}")


def get_assistant_from_config(config: Config) -> Assistant:
    logger.debug(f"[{config}] Defining LLM model={config.model}")
    llm = Ollama(model=config.model)

    storage = None
    if config.add_storage:
        db_file = str(config.dir_path / "storage.db")
        logger.debug(f"[{config}] Defining Storage {db_file=}")
        storage = SqlAssistantStorage(table_name="runs", db_file=db_file)

    return Assistant(
        name=config.name,
        description=config.description,
        instructions=config.instructions,
        llm=llm,
        markdown=config.markdown,
        storage=storage,
    )
