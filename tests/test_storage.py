from pathlib import Path

import pytest

from pas.assistant import AssistantRun
from pas.storage.sqllite import SqlAssistantStorage


@pytest.fixture(scope="module")
def storage(tmp_path_factory):
    tmp_dir = tmp_path_factory.getbasetemp()

    return SqlAssistantStorage(table_name="runs",
                               db_file=str(Path(tmp_dir) / "test_storage_db.db"))


def test_storage_init(storage):
    assert isinstance(storage, SqlAssistantStorage)


def test_storage_create(storage):
    storage.create()
    assert storage.table_exists()


def test_storage_add_run(storage):
    mock_runs = list(range(1,4))
    for run_id in mock_runs:
        storage.upsert(AssistantRun(run_id=str(run_id)))
    assert storage.read("2")
