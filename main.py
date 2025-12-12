from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatGroq(temperature=0, model="groq/compound")
# llm = ChatGroq(temperature=0, model="openai/gpt-oss-120b")
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(tools=tools, llm=llm, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    result = chain.invoke(
        input={
            "input": "What are the latest news about AI?",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
