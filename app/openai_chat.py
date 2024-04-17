import streamlit as st
from openai import OpenAI, AuthenticationError
import configparser

# Load API key
config = configparser.ConfigParser()
config.read("app/config.ini")
OPENAI_API_KEY = config["openai"]["api_key"]

client = OpenAI(api_key=OPENAI_API_KEY)

def openai_chat_ui():
    st.subheader("🤖 OpenAI Chat")

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "openai_messages" not in st.session_state:
        st.session_state["openai_messages"] = []

    for message in st.session_state["openai_messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask OpenAI"):
        st.session_state["openai_messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        try:
            response = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=st.session_state["openai_messages"],
                max_tokens=150,
                temperature=0.5
            )
            content = response.model_dump()["choices"][0]["message"]["content"]
            st.session_state["openai_messages"].append({"role": "assistant", "content": content})
            with st.chat_message("assistant"):
                st.markdown(content)
        except AuthenticationError:
            st.info("Invalid OpenAI API key! Please check your config.")
        except Exception as e:
            st.info(f"Error: {e}")
