from pas.assistant import Assistant
from pas.llm.openai import OpenAIChat

topic = "ice cream"
assistant = Assistant(llm=OpenAIChat(model="gpt-3.5-turbo"))
assistant.print_response(f"Tell me a joke about {topic}")
