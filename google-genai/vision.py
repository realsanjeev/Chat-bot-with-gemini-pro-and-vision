import configparser
import streamlit as st
import google.generativeai as genai

from PIL import Image

# read the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

GOOGLE_API_KEY = config['google']['gemini_Api_key']

# Authenticate with Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# initiate the model
model = genai.GenerativeModel('gemini-pro-vision')

def get_vision_response(image, prompt):
    try:
        if prompt != "":
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception:
        return f"You may have violated one of Safety guidelines.\n\n{response.prompt_feedback}"

# initialize out streamlit app
st.set_page_config(page_title='Gemini Vision Bot')
st.title("Gemini Pro Vision")

# initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display the vhat message from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])


# accept image
uploaded_file = st.file_uploader("Chosse a image to query....", type=["jpeg", "jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="User uploaded image",
             use_column_width=True)

prompt = st.text_input("Question abot image")
submit = st.button("Ask About Image", help="Must Upload image to proceed")


if submit and uploaded_file is not None:
    response = get_vision_response(image, prompt)
    st.write(response)
