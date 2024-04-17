import streamlit as st
from google import genai
import configparser

# Load API key
config = configparser.ConfigParser()
config.read("app/config.ini")
GOOGLE_API_KEY = config["google"]["gemini_api_key"]

client = genai.Client(api_key=GOOGLE_API_KEY)

def gemini_chat_ui():
    st.subheader("🦈 Gemini Chat")

    if "gemini_messages" not in st.session_state:
        st.session_state["gemini_messages"] = []

    for message in st.session_state["gemini_messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Gemini"):
        st.session_state["gemini_messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        try:
            response = client.models.generate_content(model="gemini-2.5-flash" ,contents=prompt)
            st.session_state["gemini_messages"].append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)
        except Exception:
            st.info("Prompt may have violated safety guidelines or there was an error.")
