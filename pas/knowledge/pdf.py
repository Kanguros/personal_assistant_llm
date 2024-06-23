from collections.abc import Iterator
from pathlib import Path

from pas.knowledge.base import AssistantKnowledge
from pas.knowledge.document import Document
from pas.knowledge.document.pdf import PDFImageReader, PDFReader


class PDFKnowledgeBase(AssistantKnowledge):
    path: str | Path
    reader: PDFReader | PDFImageReader = PDFReader()

    @property
    def document_lists(self) -> Iterator[list[Document]]:
        """Iterate over PDFs and yield lists of documents.
        Each object yielded by the iterator is a list of documents.

        Returns:
            Iterator[List[Document]]: Iterator yielding list of documents
        """

        _pdf_path: Path = Path(self.path) if isinstance(self.path, str) else self.path

        if _pdf_path.exists() and _pdf_path.is_dir():
            for _pdf in _pdf_path.glob("**/*.pdf"):
                yield self.reader.read(pdf=_pdf)
        elif _pdf_path.exists() and _pdf_path.is_file() and _pdf_path.suffix == ".pdf":
            yield self.reader.read(pdf=_pdf_path)
