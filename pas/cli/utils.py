from pas.assistant import Assistant
from pas.cli.config import AssistantConfig
from pas.llm.ollama import Ollama


def get_assistant_from_config(config: AssistantConfig) -> Assistant:
    llm = Ollama(model=config.model)
    return Assistant(
        name=config.name,
        description=config.description,
        instructions=config.instructions,
        llm=llm,
        markdown=config.markdown,
    )
