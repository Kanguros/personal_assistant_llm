from pas.assistant import Assistant
from pas.llm.cohere import CohereChat
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=CohereChat(model="command-r"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
assistant.print_response("Whats happening in France?", markdown=True, stream=False)
