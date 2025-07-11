from langgraph.graph import StateGraph, START,END
from src.langgraphagenticai.state.State import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node=BasicChatbotNode(self.llm) #calling  node

        #adding nodes
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        
        #adding edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up cinditional and direct edges between nodes.
        The chatbot node is set as the enty point.
        """

        #define toola nd toolnode
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #definr llm
        llm=self.llm

        #define chatbot node
        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        #adding nodes too create graph
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        #edges and conditional edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

    def ai_new_builder_graph(self):

        ai_news_node=AINewsNode(self.llm)
        #added the nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)

        #added the edges
        self.graph_builder.add_edge(START,"fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)


    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """

        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase=="Chatbot with Web":
            self.chatbot_with_tools_build_graph()

        if usecase=="AI News":
            self.ai_new_builder_graph()

        return self.graph_builder.compile()