# AI-Powered Todo App

A modern, Notion-inspired AI Todo app built with Streamlit, MongoDB, and Gemini (Google Generative AI).

## Features

- **Beautiful UI**: Notion-like dark theme, compact cards, and modern design.
- **AI Assistant**: Manage todos using natural language (powered by Gemini via LangChain).
- **CRUD Operations**: Add, list, complete, modify, and delete todos.
- **Summarization**: Get AI-generated summaries of your todo list.
- **Voice Input**: (Optional) Use browser-based voice-to-text in Chrome.
- **MongoDB Backend**: Todos are stored in a MongoDB Atlas database.
- **Per-user/device support**: (Planned) Each user/device can have their own todo list.

## Quickstart

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd python-todo
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file (for local dev) or use Streamlit Cloud secrets for deployment:
```
MONGODB_URI="mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>"
GEMINI_API_KEY="<your-gemini-api-key>"
GOOGLE_API_KEY="<your-google-api-key>"
```

### 4. Run the app locally
```bash
streamlit run app/main.py
```

### 5. Deploy to Streamlit Cloud
- Push your code to GitHub.
- Go to [Streamlit Cloud](https://share.streamlit.io/) and create a new app.
- Set your main file to `app/main.py`.
- Add your secrets (MongoDB URI, API keys) in the Secrets manager.

## MongoDB Atlas Setup
- Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- Add a database user with read/write access.
- In Network Access, add `0.0.0.0/0` to allow access from anywhere (for testing).
- Copy your connection string and use it as `MONGODB_URI`.

## AI & Voice
- Gemini (Google Generative AI) is used for natural language todo management and summarization.
- Voice input uses the browser's SpeechRecognition API (works best in Chrome).

## File Structure
```
python-todo/
├── app/
│   ├── main.py           # Streamlit UI
│   ├── crud.py           # CRUD operations
│   ├── database.py       # MongoDB connection
│   ├── models.py         # Pydantic models
│   └── ai/
│       ├── nlp.py        # AI logic
│       ├── llm.py        # Gemini LLM wrapper
│       ├── prompts.py    # Prompt templates
│       ├── tools.py      # Tool-calling wrappers
│       └── chains.py     # (Optional) LangChain chains
├── requirements.txt
├── .env (local only)
└── README.md
```

## Troubleshooting
- **ModuleNotFoundError**: Make sure all dependencies are in `requirements.txt`.
- **MongoDB connection errors**: Check your URI, credentials, and Atlas network access.
- **Secrets not working**: Use Streamlit Cloud's Secrets manager, not `.env`.
- **Voice input not working**: Use Chrome and allow microphone access.

## Credits
- Built with [Streamlit](https://streamlit.io/), [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), [LangChain](https://python.langchain.com/), and [Gemini](https://ai.google.dev/).

---
MIT License
