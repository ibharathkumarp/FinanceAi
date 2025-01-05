from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

web_search_Agent=Agent(
    name= "web Search agent",
    role= "search the web for the information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
finance_Agent=Agent(
    name="Finance search",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools =[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),
    ],
    instructions=["use the table to display data"],
    show_tool_calls=True,
    markdown=True,

)
multi_ai_agent=Agent(
    team=[web_search_Agent,finance_Agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)