from pas.assistant import Assistant
from pas.llm.azure import AzureOpenAIChat

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-35-turbo"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a 2 sentence quick and healthy breakfast recipe.",
    markdown=True,
    stream=False,
)
