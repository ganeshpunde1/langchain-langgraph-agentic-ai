import json
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_QUERY = (
    "Search for 3 job postings for an AI engineer using LangChain "
    "in the Bay Area on LinkedIn and list their details."
)


def create_tavily_client() -> TavilyClient:
    """Create a Tavily client using TAVILY_API_KEY from .env."""
    return TavilyClient()


def format_search_results(response: dict) -> str:
    """Turn Tavily JSON into plain text the LLM can read."""
    results = response.get("results", [])
    if not results:
        return "No search results found."

    lines = []
    for index, item in enumerate(results, start=1):
        lines.append(
            f"{index}. {item.get('title', 'No title')}\n"
            f"   URL: {item.get('url', 'N/A')}\n"
            f"   {item.get('content', '')}"
        )
    return "\n\n".join(lines)


def build_search_tool(tavily_client: TavilyClient):
    """Return a LangChain tool that searches the web with Tavily."""

    @tool
    def search(query: str) -> str:
        """Search the internet for up-to-date information."""
        print(f"Searching the web for: {query}")
        response = tavily_client.search(query=query)
        if isinstance(response, dict):
            return format_search_results(response)
        return json.dumps(response)

    return search


def build_agent(model_name: str = DEFAULT_MODEL):
    """Create an agent that can call tools and respond in natural language."""
    tavily_client = create_tavily_client()
    llm = ChatOpenAI(model=model_name)
    tools = [build_search_tool(tavily_client)]
    return create_agent(model=llm, tools=tools)


def get_agent_reply(result: dict) -> str:
    """Get the final text reply from the agent's message history."""
    messages = result.get("messages", [])
    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content:
            return message.content
    return "No reply returned by the agent."


def main(user_query: str = DEFAULT_QUERY) -> None:
    print("Hello from langchain Agent!")
    agent = build_agent()

    # The agent expects a list of chat messages, starting with the user question.
    result = agent.invoke({"messages": [HumanMessage(content=user_query)]})
    print(get_agent_reply(result))


if __name__ == "__main__":
    main()
