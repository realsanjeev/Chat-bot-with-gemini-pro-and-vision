import configparser
import streamlit as st
import google.generativeai as genai

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

GOOGLE_API_KEY = config['google']['gemini_api_key']

# Authenticate with Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Initiate the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_response_from_gemini(prompt):
    try:
        response = chat.send_message(prompt, stream=True)
        return response
    except genai.types.BlockedPromptException:
        return "**Your prompt may have violated our safety guidelines.**"
    except Exception as e:
        print(f"An error occurred: {str(e)}")  
        return f"**There was an unexpected error. Please try again later.**"


# Initialize Streamlit app
st.set_page_config(page_title="Gemini Chat bot")
st.title("Gemini Chat Bot")

# Store full message objects in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previously stored messages
with st.expander("Previous Conversation", expanded=False):
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["parts"][0]["text"])  
            
# Accept user input
if prompt := st.chat_input("Ask me Anything"):
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "parts": [{"text": prompt}]
    })

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = get_response_from_gemini(prompt)
        if isinstance(response, str):
            st.write(response)
        else:
            for chunk in response:
                st.write(chunk.text)
                st.session_state.messages.append({
                    "role": "assistant",
                    "parts": [{"text": chunk.text}]
                })

