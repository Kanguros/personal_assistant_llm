from pas.assistant import Assistant
from pas.llm.openai.like import OpenAILike
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=OpenAILike(base_url="http://localhost:8000/v1"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    debug_mode=True,
)
assistant.print_response(
    "Whats happening in France? Summarize top stories with sources.", markdown=True
)
