from pas.assistant import Assistant
from pas.llm.ollama import Ollama
from pas.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Ollama(model="openhermes"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    # debug_mode=True
)
assistant.print_response("Tell me about OpenAI Sora", markdown=True)
