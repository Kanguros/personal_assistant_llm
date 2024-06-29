from click import UsageError
from typer import Argument, Context, Option, Typer

from .config import APP_NAME, load_config, CONFIG_PATH
from .utils import set_log_level, Panel
from .utils import get_assistant_from_config
from pas.utils.log import logger

app = Typer(
    name=APP_NAME,
    rich_markup_mode="markdown",
    invoke_without_command=True,
)


@app.callback()
def main(
    ctx: Context,
    prompt: str = Argument(None, help="Prompt for LLM.", show_default=False),
    stream: bool = Option(
        True,
        "--stream/--no-stream",
        "-s/-ns",
        is_flag=True,
        rich_help_panel=Panel.OUTPUT,
    ),
    verbose: bool = Option(
        None,
        "--verbose",
        "-v",
        callback=set_log_level,
        is_flag=True,
        expose_value=False,
        is_eager=True,
        rich_help_panel=Panel.OPTIONS,
    ),
    quiet: bool = Option(
        None,
        "--quiet",
        "-q",
        callback=set_log_level,
        is_flag=True,
        expose_value=False,
        is_eager=True,
        rich_help_panel=Panel.OPTIONS,
    ),
    config=Option(
        str(CONFIG_PATH),
        "--config",
        "-c",
        # hidden=True,
        callback=load_config,
        expose_value=True,
        rich_help_panel=Panel.OPTIONS,
    ),
) -> None:
    """
    Welcome to your own Personal Assistant!

    """

    subcommands = ctx.invoked_subcommand
    if not subcommands and not prompt:
        raise UsageError("No subcommand or prompt was provided!")
    if subcommands and prompt:
        raise UsageError("Cannot combine subcommand with prompt!")

    logger.info("Welcome to Personal Assistant!")
    assistant = get_assistant_from_config(config)
    assistant.print_response(prompt, stream=stream)


if __name__ == "__main__":
    app()
