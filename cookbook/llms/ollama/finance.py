from pas.assistant import Assistant
from pas.llm.ollama import OllamaTools
from pas.tools.yfinance import YFinanceTools

print("============= llama3 finance assistant =============")
assistant = Assistant(
    llm=OllamaTools(model="llama3"),
    tools=[
        YFinanceTools(
            stock_price=True, analyst_recommendations=True, stock_fundamentals=True
        )
    ],
    show_tool_calls=True,
)
assistant.cli_app(markdown=True)
