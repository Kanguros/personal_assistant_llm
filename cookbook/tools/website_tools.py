from pas.assistant import Assistant
from pas.tools.website import WebsiteTools

assistant = Assistant(tools=[WebsiteTools()], show_tool_calls=True)
assistant.print_response(
    "Search web page: 'https://docs.phidata.com/introduction'", markdown=True
)
