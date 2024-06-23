from os import getenv

import vertexai

from pas.assistant import Assistant
from pas.llm.gemini import Gemini
from pas.tools.duckduckgo import DuckDuckGo

# *********** Initialize VertexAI ***********
vertexai.init(project=getenv("PROJECT_ID"), location=getenv("LOCATION"))

assistant = Assistant(
    llm=Gemini(model="gemini-pro"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
)
assistant.print_response(
    "Whats happening in France?  Summarize top 10 stories with sources", markdown=True
)
