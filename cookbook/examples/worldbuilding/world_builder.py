from pydantic import BaseModel, Field
from rich.pretty import pprint

from pas.assistant import Assistant
from pas.llm.ollama import Ollama


class World(BaseModel):
    name: str = Field(
        ...,
        description="This is the name of the world. Be as creative as possible. Do not use simple names like Futura, Earth etc.",
    )
    characteristics: list[str] = Field(
        ...,
        description="These are the characteristics of the world. Be as creative as possible.",
    )
    drugs: list[str] = Field(
        ...,
        description="These are the drugs the people in the world use. Be as creative as possible.",
    )
    languages: list[str] = Field(
        ...,
        description="These are the languages spoken in the world. Be as creative as possible.",
    )
    history: str = Field(
        ...,
        description="This is a detailed history of the world. Be as creative as possible. Use events, wars, etc. to make it interesting.",
    )


pprint(
    Assistant(
        llm=Ollama(model="openhermes", options={"temperature": 0.1}), output_model=World
    ).run()
)
