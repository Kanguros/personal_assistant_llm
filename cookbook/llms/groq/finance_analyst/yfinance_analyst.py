from pas.assistant import Assistant
from pas.llm.groq import Groq
from pas.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=Groq(model="llama3-70b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
            company_info=True,
        )
    ],
    show_tool_calls=True,
    markdown=True,
)
assistant.cli_app(user="Groq")
