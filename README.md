# Unified AI Chat Interface

A **Streamlit-powered web app** that integrates **OpenAI GPT** and **Google Gemini (Gemini Pro)** chat models into one seamless interface. Users can easily interact with either AI model, with separate chat histories preserved for each.

## Features

* **Single interface** for multiple AI models
* **OpenAI GPT** (GPT-3.5 / GPT-4) integration
* **Google Gemini** integration
* **Independent chat histories** for OpenAI and Gemini
* Interactive chat messages via Streamlit UI
* Configurable API keys using `config.ini` or Streamlit secrets
* Easy to expand with additional AI backends


## Folder Structure

```
.
├── app/
│   ├── __init__.py
│   ├── openai_chat.py      # OpenAI GPT chat module
│   ├── gemini_chat.py      # Google Gemini chat module
│   └── config.ini          # API keys configuration
├── main.py                 # App entry point
└── requirements.txt
```


## Getting Started

1. **Set up a virtual environment** (recommended but optional):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure API keys**:

Copy `app/config.ini.example` to `app/config.ini`, then add your API keys for OpenAI and Google Gemini:

```ini
[openai]
api_key = YOUR_OPENAI_API_KEY

[google]
gemini_api_key = YOUR_GOOGLE_GEMINI_KEY
```

> Alternatively, use **Streamlit secrets** when deploying on Streamlit Cloud.


4. **Run the app**:

```bash
streamlit run main.py
```

* Open the URL in your browser (typically `http://localhost:8501`)
* Choose either **OpenAI GPT** or **Google Gemini** to begin chatting


## Usage

* **OpenAI GPT**: Enter a query in the “Ask OpenAI” input box. The AI responds and maintains a conversation history.
* **Google Gemini**: Type a question in the “Ask Gemini” input box. Responses will be streamed and shown interactively.


## Extending the App

* Add new AI backends by creating additional chat modules (e.g., `app/your_ai.py`)
* Add extra configuration sections in `config.ini`
* Use session state to keep separate chat histories for each model

### References:

* [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
* [OpenAI API Documentation](https://platform.openai.com/docs/overview)
