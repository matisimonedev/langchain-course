from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

# from tavily import TavilyClient

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """Tool that searches for information on the web.
#     Args:
#         query (str): The search query.
#     Returns:
#         str: The search results.
#     """
#     print(f"You searched for: {query}")
#     return tavily.search(query=query)

# # llm = ChatGroq(temperature=0, model="groq/compound")
# llm = ChatGroq(temperature=0, model="openai/gpt-oss-120b")
# tools = [search]
# agent = create_agent(model=llm, tools=tools)

class Source(BaseModel):
    """Schema for a source user by the agent"""
    # name: str = Field(description="Name of the source")
    url: str = Field(description="URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent response"""
    answer: str = Field(description="Answer to the user")
    sources: List[Source] = Field(default_factory=list, description="Sources used to answer the user")


llm = ChatGroq(temperature=0, model="openai/gpt-oss-120b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="find 2 jobs for angular front end developers in linkedin adn give me just the links"
            )
        }
    )
    print(result)
    # print(result['structured_response'].answer)
    # print(result['structured_response'].sources)


if __name__ == "__main__":
    main()
