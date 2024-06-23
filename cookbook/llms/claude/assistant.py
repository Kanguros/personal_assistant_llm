from pas.assistant import Assistant
from pas.llm.anthropic import Claude
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Claude(model="claude-3-opus-20240229"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
assistant.print_response("Whats happening in France?", markdown=True)
