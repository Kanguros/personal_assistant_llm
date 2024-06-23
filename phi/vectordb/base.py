from abc import ABC, abstractmethod

from phi.document import Document


class VectorDb(ABC):
    """Base class for managing Vector Databases"""

    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def doc_exists(self, document: Document) -> bool:
        raise NotImplementedError

    @abstractmethod
    def name_exists(self, name: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def insert(self, documents: list[Document]) -> None:
        raise NotImplementedError

    def upsert_available(self) -> bool:
        return False

    @abstractmethod
    def upsert(self, documents: list[Document]) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str, limit: int = 5) -> list[Document]:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def optimize(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> bool:
        raise NotImplementedError
