from pas.assistant import Assistant
from pas.llm.groq import Groq
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Groq(model="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always search the web for information"],
    show_tool_calls=True,
)
assistant.cli_app(markdown=True, stream=False)
# assistant.print_response("Whats happening in France?", markdown=True, stream=False)
