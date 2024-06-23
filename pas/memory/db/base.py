from abc import ABC, abstractmethod

from pas.memory.row import MemoryRow


class MemoryDb(ABC):
    """Base class for the Memory Database."""

    @abstractmethod
    def create_table(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def memory_exists(self, memory: MemoryRow) -> bool:
        raise NotImplementedError

    @abstractmethod
    def read_memories(
        self,
        user_id: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
    ) -> list[MemoryRow]:
        raise NotImplementedError

    @abstractmethod
    def upsert_memory(self, memory: MemoryRow) -> MemoryRow | None:
        raise NotImplementedError

    @abstractmethod
    def delete_memory(self, id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_table(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def table_exists(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def clear_table(self) -> bool:
        raise NotImplementedError
