from pydantic import BaseModel, ConfigDict


class Embedder(BaseModel):
    """Base class for managing embedders"""

    dimensions: int = 1536

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_embedding(self, text: str) -> list[float]:
        raise NotImplementedError

    def get_embedding_and_usage(self, text: str) -> tuple[list[float], dict | None]:
        raise NotImplementedError
