from pathlib import Path
from typing import IO, Any

from pas.knowledge.document.base import Document
from pas.knowledge.document.reader import Reader
from pas.utils.log import logger


class PDFReader(Reader):
    """Reader for PDF files"""

    def read(self, pdf: str | Path | IO[Any]) -> list[Document]:
        if not pdf:
            raise ValueError("No pdf provided")

        try:
            from pypdf import PdfReader as DocumentReader
        except ImportError:
            raise ImportError("`pypdf` not installed")

        doc_name = ""
        try:
            if isinstance(pdf, str):
                doc_name = pdf.split("/")[-1].split(".")[0].replace(" ", "_")
            else:
                doc_name = pdf.name.split(".")[0]
        except Exception:
            doc_name = "pdf"

        logger.info(f"Reading: {doc_name}")
        doc_reader = DocumentReader(pdf)

        documents = [
            Document(
                name=doc_name,
                id=f"{doc_name}_{page_number}",
                meta_data={"page": page_number},
                content=page.extract_text(),
            )
            for page_number, page in enumerate(doc_reader.pages, start=1)
        ]
        if self.chunk:
            chunked_documents = []
            for document in documents:
                chunked_documents.extend(self.chunk_document(document))
            return chunked_documents
        return documents


class PDFImageReader(Reader):
    """Reader for PDF files with text and images extraction"""

    def read(self, pdf: str | Path | IO[Any]) -> list[Document]:
        if not pdf:
            raise ValueError("No pdf provided")

        try:
            import rapidocr_onnxruntime as rapidocr
            from pypdf import PdfReader as DocumentReader
        except ImportError:
            raise ImportError("`pypdf` or `rapidocr_onnxruntime` not installed")

        doc_name = ""
        try:
            if isinstance(pdf, str):
                doc_name = pdf.split("/")[-1].split(".")[0].replace(" ", "_")
            else:
                doc_name = pdf.name.split(".")[0]
        except Exception:
            doc_name = "pdf"

        logger.info(f"Reading: {doc_name}")
        doc_reader = DocumentReader(pdf)

        # Initialize RapidOCR
        ocr = rapidocr.RapidOCR()

        documents = []
        for page_number, page in enumerate(doc_reader.pages, start=1):
            page_text = page.extract_text() or ""
            images_text_list: list = []

            for image_object in page.images:
                image_data = image_object.data

                # Perform OCR on the image
                ocr_result, elapse = ocr(image_data)

                # Extract text from OCR result
                if ocr_result:
                    images_text_list += [item[1] for item in ocr_result]

            images_text: str = "\n".join(images_text_list)
            content = page_text + "\n" + images_text

            documents.append(
                Document(
                    name=doc_name,
                    id=f"{doc_name}_{page_number}",
                    meta_data={"page": page_number},
                    content=content,
                ),
            )

        if self.chunk:
            chunked_documents = []
            for document in documents:
                chunked_documents.extend(self.chunk_document(document))
            return chunked_documents

        return documents
