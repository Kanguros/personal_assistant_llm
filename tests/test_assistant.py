import pytest

from phi.assistant import Assistant


@pytest.mark.parametrize("kwargs", [
    {},
])
def test_assistant_init(kwargs: dict):
    assistant = Assistant(**kwargs)
    assert isinstance(assistant, assistant.Assistant)
