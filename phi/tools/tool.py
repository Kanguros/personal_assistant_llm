from typing import Any

from pydantic import BaseModel


class Tool(BaseModel):
    """Model for Tools"""

    # The type of tool
    type: str
    # The function to be called if type = "function"
    function: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
