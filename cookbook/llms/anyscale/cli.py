from pas.assistant import Assistant
from pas.llm.anyscale import Anyscale

assistant = Assistant(llm=Anyscale(model="mistralai/Mixtral-8x7B-Instruct-v0.1"))
assistant.cli_app(markdown=True)
