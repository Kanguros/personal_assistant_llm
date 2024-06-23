from pas.assistant import Assistant
from pas.tools.apify import ApifyTools

assistant = Assistant(tools=[ApifyTools()], show_tool_calls=True)
assistant.print_response(
    "Tell me about https://docs.phidata.com/introduction", markdown=True
)
