from pas.assistant import Assistant
from pas.llm.together import Together
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(llm=Together(), tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response(
    "Whats happening in France? Summarize top stories with sources.",
    markdown=True,
    stream=False,
)
