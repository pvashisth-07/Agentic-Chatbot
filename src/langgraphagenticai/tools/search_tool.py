from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """Returns the list of tools used in the chatbot"""

    tools=[TavilySearchResults(max_results=5)]

    return tools

def create_tool_node(tools):
    """
    creates and return a tool node for graph.
    """

    return ToolNode(tools=tools)