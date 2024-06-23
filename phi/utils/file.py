from typing import List, Optional, Any
from phi.utils.log import logger
from pydantic import BaseModel


class File(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    columns: Optional[List[str]] = None
    path: Optional[str] = None
    type: str = "FILE"

    def get_metadata(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)


class CsvFile(File):
    path: str
    type: str = "CSV"

    def get_metadata(self) -> dict[str, Any]:
        if self.name is None:
            from pathlib import Path

            self.name = Path(self.path).name

        if self.columns is None:
            try:
                # Get the columns from the file
                import csv

                with open(self.path) as csvfile:
                    dict_reader = csv.DictReader(csvfile)
                    if dict_reader.fieldnames is not None:
                        self.columns = list(dict_reader.fieldnames)
            except Exception as e:
                logger.debug(f"Error getting columns from file: {e}")

        return self.model_dump(exclude_none=True)


class TextFile(File):
    path: str
    type: str = "TEXT"

    def get_metadata(self) -> dict[str, Any]:
        if self.name is None:
            from pathlib import Path

            self.name = Path(self.path).name
        return self.model_dump(exclude_none=True)
