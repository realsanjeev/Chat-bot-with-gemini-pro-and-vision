### Google Gemini Chat Bot

Each script within this repository represents a distinct application with unique functionality.

**Step 1: Activate the Virtual Environment**

Begin by creating and activating the virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate
```

**Step 2: Install Dependencies**

Install the necessary dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

**Step 3: Run the Application**

Launch the desired application with the corresponding command:
1. To run the bot for question answering (text), use:
   ```bash
   streamlit run app.py
   ```
2. To run the bot for vision, use:
   ```bash
   streamlit run vision.py
   ```
3. To run the chat app, which responds with a chain of thought and allows for follow-up questions, use:
   ```bash
   streamlit run chat.py
   ```