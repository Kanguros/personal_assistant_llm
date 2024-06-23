from pas.assistant import Assistant
from pas.llm.ollama import Ollama
from pas.tools.duckduckgo import DuckDuckGo

hermes = Assistant(
    llm=Ollama(model="openhermes"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
hermes.print_response(
    "Whats happening in France? Summarize top stories with sources.", markdown=True
)
