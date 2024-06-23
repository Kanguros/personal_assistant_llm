from collections.abc import Iterator
from pathlib import Path

from phi.document import Document
from phi.document.text import TextReader
from phi.knowledge.base import AssistantKnowledge


class TextKnowledgeBase(AssistantKnowledge):
    path: str | Path
    formats: list[str] = [".txt"]
    reader: TextReader = TextReader()

    @property
    def document_lists(self) -> Iterator[list[Document]]:
        """Iterate over text files and yield lists of documents.
        Each object yielded by the iterator is a list of documents.

        Returns:
            Iterator[List[Document]]: Iterator yielding list of documents
        """

        _file_path: Path = Path(self.path) if isinstance(self.path, str) else self.path

        if _file_path.exists() and _file_path.is_dir():
            for _file in _file_path.glob("**/*"):
                if _file.suffix in self.formats:
                    yield self.reader.read(path=_file)
        elif (
            _file_path.exists()
            and _file_path.is_file()
            and _file_path.suffix in self.formats
        ):
            yield self.reader.read(path=_file_path)
