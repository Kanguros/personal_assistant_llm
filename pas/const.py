"""
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\assistant\\duckdb.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\knowledge\\website.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\knowledge\\document\\website.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\knowledge\\embedder\\azure_openai.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\knowledge\\embedder\\openai.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\azure\\openai_chat.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\azure\\__init__.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\ollama\\openai.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\openai\\chat.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\openai\\like.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\llm\\openai\\__init__.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\tools\\duckdb.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\tools\\duckduckgo.py]
FAILED tests/test_imports.py::test_modules_import[D:\\Projects\\phidata\\pas\\tools\\website.py]

"""

DEPENDENCY_GROUP_WEBTOOLS = "webtool"
DEPENDENCY_GROUP_FILES = "files"
DEPENDENCY_GROUP_OPENAI = "openai"

IMPORT_ERROR = lambda package, group: f"The `{package}` package is not installed. Please install it via `poetry install --with={group}`"