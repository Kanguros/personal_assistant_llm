from pas.assistant import Assistant
from pas.llm.azure import AzureOpenAIChat

assistant = Assistant(
    llm=AzureOpenAIChat(model="gpt-35-turbo"),  # model="deployment_name"
    description="You help people with their health and fitness goals.",
)
assistant.cli_app(markdown=True)
