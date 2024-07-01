from pas_cli.config import Config


class HelpfulAssistant(Config):
    name: str = "Helpful Assistant"
    description: str = "You are a helpful assistant."
    instructions: list[str] = [
        "Provide detailed and accurate responses.",
        "Assist the user with their queries."
    ]