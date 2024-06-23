from pas.assistant import Assistant
from pas.llm.fireworks import Fireworks

assistant = Assistant(
    llm=Fireworks(),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a quick healthy breakfast recipe.", markdown=True, stream=False
)
