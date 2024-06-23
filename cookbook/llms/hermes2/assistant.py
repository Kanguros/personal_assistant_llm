from pas.assistant import Assistant
from pas.llm.ollama import Hermes
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Hermes(model="adrienbrault/nous-hermes2pro:Q8_0"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
assistant.print_response("Whats happening in France?", markdown=True)
