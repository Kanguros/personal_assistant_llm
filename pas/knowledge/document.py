from collections.abc import Iterator

from pas.knowledge.document import Document
from pas.knowledge.base import AssistantKnowledge


class DocumentKnowledgeBase(AssistantKnowledge):
    documents: list[Document]

    @property
    def document_lists(self) -> Iterator[list[Document]]:
        """Iterate over documents and yield lists of documents.
        Each object yielded by the iterator is a list of documents.

        Returns:
            Iterator[List[Document]]: Iterator yielding list of documents
        """

        for _document in self.documents:
            yield [_document]
