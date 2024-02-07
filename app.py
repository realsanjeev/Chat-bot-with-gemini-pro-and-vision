import configparser
import streamlit as st
import google.generativeai as genai

# Specify the full path to the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

GOOGLE_API_KEY = config['google']['gemini_api_key']

# Authenticate with Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Initiate the model
model = genai.GenerativeModel('gemini-pro')

def get_response_from_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception:
        return f"**Your question may have violated one of our safety guidelines.**\n\n{response.prompt_feedback}"

# initialize our Streamlit app
st.set_page_config(page_title="Gemini Q/A Bot", page_icon="🦈")
st.title("Gemini Assistant")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from the history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# accept user input
if prompt := st.chat_input("Ask Me anything"):
    # add user message to chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # display assistant response in chat message container
    with st.chat_message("assistant"):
        response = get_response_from_gemini(prompt)
        st.write(response)
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
