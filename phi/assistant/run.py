from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class AssistantRun(BaseModel):
    """Assistant Run that is stored in the database"""

    # Assistant name
    name: str | None = None
    # Run UUID
    run_id: str
    # Run name
    run_name: str | None = None
    # ID of the user participating in this run
    user_id: str | None = None
    # LLM data (name, model, etc.)
    llm: dict[str, Any] | None = None
    # Assistant Memory
    memory: dict[str, Any] | None = None
    # Metadata associated with this assistant
    assistant_data: dict[str, Any] | None = None
    # Metadata associated with this run
    run_data: dict[str, Any] | None = None
    # Metadata associated the user participating in this run
    user_data: dict[str, Any] | None = None
    # Metadata associated with the assistant tasks
    task_data: dict[str, Any] | None = None
    # The timestamp of when this run was created
    created_at: datetime | None = None
    # The timestamp of when this run was last updated
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

    def serializable_dict(self) -> dict[str, Any]:
        _dict = self.model_dump(exclude={"created_at", "updated_at"})
        _dict["created_at"] = self.created_at.isoformat() if self.created_at else None
        _dict["updated_at"] = self.updated_at.isoformat() if self.updated_at else None
        return _dict

    def assistant_dict(self) -> dict[str, Any]:
        _dict = self.model_dump(exclude={"created_at", "updated_at", "task_data"})
        _dict["created_at"] = self.created_at.isoformat() if self.created_at else None
        _dict["updated_at"] = self.updated_at.isoformat() if self.updated_at else None
        return _dict
