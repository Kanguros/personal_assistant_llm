from pas.assistant import Assistant
from pas.llm.mistral import Mistral
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Mistral(model="mistral-large-latest"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    debug_mode=True,
)
assistant.print_response(
    "Whats happening in France? Summarize top 2 stories", markdown=True
)
