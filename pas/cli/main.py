from click import UsageError
from typer import Argument, Context, Option, Typer

from pas.cli.config import APP_NAME, load_config
from pas.cli.console import set_log_level, Panel
from pas.cli.utils import get_assistant_from_config
from pas.utils.log import logger

app = Typer(
    name=APP_NAME,
    rich_markup_mode="markdown",
    invoke_without_command=True,
)


@app.callback()
def main(
        ctx: Context,
        prompt: str = Argument(None, help="Prompt for LLM."),
        stream: int = Option(
            None,
            "--stream/--no-stream",
            "-s/-ns",
            is_flag=True,
            rich_help_panel=Panel.OUTPUT,
        ),
        verbose: int = Option(
            None,
            "--verbose",
            "-v",
            callback=set_log_level,
            is_flag=True,
            expose_value=False,
            is_eager=True,
            rich_help_panel=Panel.OPTIONS,
        ),
        quiet: int = Option(
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
            None,
            "--config",
            "-c",
            count=True,
            hidden=True,
            callback=load_config,
            expose_value=True,
            rich_help_panel=Panel.OPTIONS,

        ),
) -> None:
    """
    Welcome to your own Personal Assistant!

    """
    logger.info("Welcome to Personal Assistant!")
    subcommands = ctx.invoked_subcommand
    if not subcommands and not prompt:
        raise UsageError("No subcommand or prompt was provided!")
    if subcommands and prompt:
        raise UsageError("Cannot combine subcommand with prompt!")

    assistant = get_assistant_from_config(config.default_assistant)
    assistant.print_response(prompt, stream=stream)


if __name__ == "__main__":
    app()
