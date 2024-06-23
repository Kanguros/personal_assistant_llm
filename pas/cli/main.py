from click import UsageError
from typer import Argument, Context, Option, Typer

from pas.cli.config import APP_NAME, Panel, load_config, set_debug
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
    verbose: int = Option(
        None,
        "--verbose",
        "-v",
        callback=set_debug,
        count=True,
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
    ),
) -> None:
    """
    Welcome to your own Personal Assistant!

    """
    logger.info("Welcome to Personal Assistant!")
    subcommands = ctx.invoked_subcommand
    if subcommands and prompt:
        raise UsageError("Cannot combine subcommand with prompt!")
    if not subcommands and not prompt:
        raise UsageError("No subcommand or prompt was provided!")


if __name__ == "__main__":
    app()
