#### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the question-answer app using OpenAI and LangChain. After running the app, enter your OpenAI API key from the sidebar:

```bash
streamlit run langchain_qa_openai.py
```

or

Run a chat-like app with OpenAI (Make sure to add your Streamlit secrets in `.streamlit/secrets.toml` in the project directory):

```bash
streamlit run chat_GPT.py
```

<details>
  <summary>ChainLit Running App Info (not included)</summary>

```bash
pip install -U langchain
pip install -U chatlit
```

Run the ChatLit app with the `-w` flag to watch changes in the script and automatically reload the browser:

```bash
chainlit run <app_name> -w
```

#### Example Usage

```python
from langchain.prompts import PromptTemplate

template = """Question: {question}

Answer: Let's think step by step
"""
# The template is used for templating
# In the template variable, "{question}" is replaced by the value given below
print(template.format(question="What is your name"))
```

This provides a brief guide on installing dependencies, running the question-answer and chat-like apps, and a simple example of using the LangChain prompt template.
</details>

