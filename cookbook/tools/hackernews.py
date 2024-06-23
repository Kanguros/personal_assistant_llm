from pas.assistant import Assistant
from pas.tools.hackernews import HackerNews

hn_assistant = Assistant(
    name="Hackernews Team",
    tools=[HackerNews()],
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)
hn_assistant.print_response(
    "Write an engaging summary of the "
    "users with the top 2 stories on hackernews. "
    "Please mention the stories as well.",
)
