from pas.assistant import Assistant
from pas.llm.openai import OpenAIChat
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("Search for news from France and write a short poem about it.")
