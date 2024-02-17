import streamlit as st
from openai import OpenAI
from openai import AuthenticationError

# initialize out streamlit app
st.set_page_config(page_title="ChatGPT - clone", page_icon="🤖")
st.title("🤖ChatGPT clone")


# Use the OPENAI key secret from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a model for OpenAI
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# For displaying chat messages from history on app run
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What can I help you with?"):
    # Display user Prompt
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        # Get response from OpenAI
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages,
            max_tokens=150,
            temperature=0.5,  
            top_p=1,
        )

        # Add AI message to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response.model_dump()["choices"][0]["message"]["content"]
        })

        # Display AI message
        with st.chat_message("assistant"):
            st.markdown(response.model_dump()["choices"][0]["message"]["content"])
    except AuthenticationError:
        st.info("Invalid api_key! 💀[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
    except Exception as err:
        st.info(f"Error: {err}")
