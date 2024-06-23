from typing import Any

from pydantic import BaseModel


class Memory(BaseModel):
    """Model for LLM memories"""

    memory: str
    id: str | None = None
    topic: str | None = None
    input: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
