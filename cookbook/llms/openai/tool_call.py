from pas.assistant import Assistant
from pas.llm.openai import OpenAIChat
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4-turbo"), tools=[DuckDuckGo()], show_tool_calls=True
)
assistant.print_response("Whats happening in France?", markdown=True)
