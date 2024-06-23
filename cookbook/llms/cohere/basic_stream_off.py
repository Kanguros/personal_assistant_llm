from pas.assistant import Assistant
from pas.llm.cohere import CohereChat

assistant = Assistant(
    llm=CohereChat(model="command-r"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a quick healthy breakfast recipe.", markdown=True, stream=False
)
