from pathlib import Path

from pas.assistant import Assistant
from pas.llm.ollama import Ollama

assistant = Assistant(llm=Ollama(model="llava"))

image_path = Path(__file__).parent / "test_image.jpeg"
assistant.print_response(
    "Whats in the image?",
    images=[image_path.read_bytes()],
    markdown=True,
)
