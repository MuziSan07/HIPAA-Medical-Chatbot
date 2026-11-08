# HIPAA-Aware Medical Chatbot

A privacy-conscious medical **information** chatbot built with **FastAPI** and
**LangChain + Groq**. It answers general medical questions through a clean
Bootstrap chat UI, and is organised using the **Model-View-Controller (MVC)**
pattern.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-async-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Important disclaimer

> This project is for **educational and informational purposes only**. It is
> **not** a medical device and does **not** provide diagnosis or treatment.
>
> It is **"HIPAA-aware"** — designed to minimise and never store personal health
> information (PHI) — but it is **not a certified HIPAA-compliant system**. It
> sends questions to a third-party model provider (Groq) and has no Business
> Associate Agreement (BAA), authentication, or audit controls. **Do not enter
> real PHI**, and always consult a qualified healthcare professional for personal
> medical concerns.

---

## Features

- **Medical Q&A** through a single `/chat` endpoint.
- **Privacy-conscious system prompt** — non-diagnostic, PHI-minimising.
- **Standing disclaimer** returned with every API response and shown in the UI.
- **Input validation** — question length limits via Pydantic.
- **Explicit CORS allow-list** (never `*`).
- **Responsive chat UI** with HTML output escaping to prevent injection.

---

## Architecture (MVC)

| Layer | Responsibility | Files |
|-------|----------------|-------|
| **Model** | Data schemas and the LangChain/Groq domain logic | `app/models/schemas.py`, `app/models/chatbot_model.py` |
| **View** | Response formatting and the frontend UI | `app/views/responses.py`, `app/views/static/index.html` |
| **Controller** | HTTP routes wiring requests to model + view | `app/controllers/chat_controller.py` |
| **App** | Factory, CORS, static mounting, config | `app/main.py`, `app/config.py` |

```
HIPAA-Medical-Chatbot/
├── app/
│   ├── main.py                     # App factory (uvicorn app.main:app)
│   ├── config.py                   # Environment-driven settings
│   ├── models/
│   │   ├── schemas.py              # ChatRequest / ChatResponse
│   │   └── chatbot_model.py        # LangChain chain + generate_answer()
│   ├── views/
│   │   ├── responses.py            # Response formatting + disclaimer
│   │   └── static/
│   │       └── index.html          # Frontend chat UI
│   └── controllers/
│       └── chat_controller.py      # Routes: GET / and POST /chat
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## Getting started

### 1. Install

```bash
git clone https://github.com/MuziSan07/HIPAA-Medical-Chatbot.git
cd HIPAA-Medical-Chatbot

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Edit .env and set your GROQ_API_KEY
```

Get a free API key at <https://console.groq.com/>.

### 3. Run

```bash
uvicorn app.main:app --reload
```

Then open <http://127.0.0.1:8000/> for the chat UI, or
<http://127.0.0.1:8000/docs> for the interactive API docs.

---

## API reference

### `POST /chat`

Request:

```json
{ "question": "What are common symptoms of dehydration?" }
```

Response:

```json
{
  "response": "The chatbot's educational answer ...",
  "disclaimer": "This chatbot provides general educational information only ..."
}
```

---

## Tech stack

- **Backend:** FastAPI, Uvicorn
- **LLM orchestration:** LangChain (`langchain-core`, `langchain-groq`)
- **Model provider:** Groq (default: `llama-3.3-70b-versatile`)
- **Frontend:** HTML, Bootstrap 5, jQuery (loaded from CDNs)
- **Config:** python-dotenv

---

## Future work

- Add authentication and per-user rate limiting on `/chat`.
- Add automated tests (pytest) and CI.
- Optional: self-hosted model to avoid sending data to third parties.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.
