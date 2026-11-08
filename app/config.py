"""Environment-driven configuration.

Values are read from the environment (see .env.example). Nothing secret is
hard-coded; the Groq API key must be supplied via the environment.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# --- Paths -----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent          # the app/ package
STATIC_DIR = BASE_DIR / "views" / "static"          # frontend (View layer)

# --- Groq / model ----------------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
TEMPERATURE = float(os.getenv("GROQ_TEMPERATURE", "0.1"))

# --- Request limits --------------------------------------------------------
MAX_QUESTION_LENGTH = int(os.getenv("MAX_QUESTION_LENGTH", "2000"))

# --- CORS ------------------------------------------------------------------
# Explicit allow-list; never defaults to "*".
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS", "http://localhost:8000,http://127.0.0.1:8000"
    ).split(",")
    if origin.strip()
]
