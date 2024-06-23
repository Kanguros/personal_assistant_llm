from pas.assistant import Assistant
from pas.llm.anyscale import Anyscale

assistant = Assistant(
    llm=Anyscale(model="mistralai/Mixtral-8x7B-Instruct-v0.1"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a 2 sentence quick and healthy breakfast recipe.",
    markdown=True,
    stream=False,
)
