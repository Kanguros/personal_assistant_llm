import importlib.util
from pathlib import Path
from typing import List

import pytest

import phi


def get_package_python_files() -> List[Path]:
    python_files = Path(phi.__file__).parent.rglob("**/*.py")
    return [file for file in python_files if file.is_file()]


python_files = get_package_python_files()


@pytest.mark.parametrize(
    "module_path",
    [*python_files],
    ids=[str(f) for f in python_files]
)
def test_modules_import(module_path):
    try:
        spec = importlib.util.spec_from_file_location(str(module_path.stem), str(module_path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as ex:
        raise AssertionError(str(ex))
