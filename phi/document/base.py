from typing import Any

from pydantic import BaseModel, ConfigDict

from phi.embedder import Embedder


class Document(BaseModel):
    """Model for managing a document"""

    content: str
    id: str | None = None
    name: str | None = None
    meta_data: dict[str, Any] = {}
    embedder: Embedder | None = None
    embedding: list[float] | None = None
    usage: dict[str, Any] | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def embed(self, embedder: Embedder | None = None) -> None:
        """Embed the document using the provided embedder"""

        _embedder = embedder or self.embedder
        if _embedder is None:
            raise ValueError("No embedder provided")

        self.embedding, self.usage = _embedder.get_embedding_and_usage(self.content)

    def to_dict(self) -> dict[str, Any]:
        """Returns a dictionary representation of the document"""

        return self.model_dump(
            include={"name", "meta_data", "content"}, exclude_none=True
        )

    @classmethod
    def from_dict(cls, document: dict[str, Any]) -> "Document":
        """Returns a Document object from a dictionary representation"""

        return cls.model_validate(**document)

    @classmethod
    def from_json(cls, document: str) -> "Document":
        """Returns a Document object from a json string representation"""

        return cls.model_validate_json(document)
