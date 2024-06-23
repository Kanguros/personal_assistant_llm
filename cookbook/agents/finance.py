from pas.assistant import Assistant
from pas.llm.openai import OpenAIChat
from pas.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    show_tool_calls=True,
)
assistant.print_response("Compare NVDA to TSLA. Use every tool you have", markdown=True)
