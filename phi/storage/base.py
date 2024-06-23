from abc import ABC, abstractmethod

from phi.assistant.run import AssistantRun


class AssistantStorage(ABC):
    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self, run_id: str) -> AssistantRun | None:
        raise NotImplementedError

    @abstractmethod
    def get_all_run_ids(self, user_id: str | None = None) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def get_all_runs(self, user_id: str | None = None) -> list[AssistantRun]:
        raise NotImplementedError

    @abstractmethod
    def upsert(self, row: AssistantRun) -> AssistantRun | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError
