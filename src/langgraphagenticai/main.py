import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graphbuilder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_results import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    #Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
        return
    
    #text from user
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message=st.chat_input("Enter your message:")

    if user_message:
        try:
            #configuaring llms
            obj_llm_config=GroqLLM(user_controls_inputs=user_input)
            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("LLM Model could not be initialsed.")
                return
            
            #initialising usecase
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("No usecase found.")
                return
            
            #graph builder
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                print(f"Graph setup failed. Error: {e}")
        except Exception as e:
            print(f"Error {e}")
