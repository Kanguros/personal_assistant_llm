from pas.assistant import Assistant
from pas.llm.groq import Groq

assistant = Assistant(
    llm=Groq(model="mixtral-8x7b-32768"),
    description="You help people with their health and fitness goals.",
)
assistant.print_response(
    "Share a quick healthy breakfast recipe.", markdown=True, stream=False
)
