import streamlit as st
from app.openai_chat import openai_chat_ui
from app.gemini_chat import gemini_chat_ui

st.set_page_config(page_title="Unified AI Chat", page_icon="🤖🦈")

st.title("Unified AI Chat Interface")
st.write("Choose a model to chat with:")

model_choice = st.radio("Select AI Model:", ["OpenAI GPT", "Google Gemini"])

if model_choice == "OpenAI GPT":
    openai_chat_ui()
else:
    gemini_chat_ui()