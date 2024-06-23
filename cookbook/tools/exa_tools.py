import os

from pas.assistant import Assistant
from pas.tools.exa import ExaTools

os.environ["EXA_API_KEY"] = "your api key"

assistant = Assistant(
    tools=[ExaTools(include_domains=["cnbc.com", "reuters.com", "bloomberg.com"])],
    show_tool_calls=True,
)
assistant.print_response("Search for AAPL news", debug_mode=True, markdown=True)
