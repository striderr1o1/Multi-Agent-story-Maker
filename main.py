import os
from crewai import Agent, Task, Crew, LLM
#from langchain_ollama import ChatOllama
from langchain_community.chat_models import ChatOllama
from crewai.cli.constants import ENV_VARS
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from crewlogic import run_crew
import streamlit as st


llm = LLM(
    model="ollama/gemma3:1b",
    base_url="http://localhost:11434"
    
)

st.set_page_config(page_title="CrewAI Story Generator")
st.title("🧠 Multi-Agent Story Generator")

topic = st.text_input("Enter a story topic:")

if st.button("Generate Story") and topic:
    with st.spinner("Agents are working..."):
        output = run_crew(llm, topic)
    st.subheader("📝 Story Output")
    st.write(output)

