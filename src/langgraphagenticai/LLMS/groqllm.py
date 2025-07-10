import streamlit as st
import os
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_inputs):
        self.user_controls_input=user_controls_inputs

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Please enter the Groq API Key!!!")
            
            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error Occured with exception {e}")
        return llm