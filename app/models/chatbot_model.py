"""Chatbot domain logic (Model layer).

Wraps the LangChain pipeline (prompt | LLM | output parser) around the Groq
model. The chain is built lazily so that importing this module does not require
network access or a configured API key.
"""

from .. import config

# System prompt: privacy-conscious and explicitly non-diagnostic. The chatbot is
# an educational assistant, not a HIPAA-compliant covered-entity system.
SYSTEM_PROMPT = (
    "You are a privacy-conscious, HIPAA-aware medical information assistant. "
    "Provide general, medically accurate, and reliable educational information. "
    "Do NOT diagnose, prescribe, or provide individualized medical advice, and "
    "do NOT request, store, or repeat personal health information (PHI). "
    "If a user shares personal or identifying health details, gently remind them "
    "not to, and answer only in general terms. Always encourage users to consult "
    "a qualified healthcare professional for personal medical concerns."
)

_chain = None


def get_chain():
    """Build and cache the LangChain pipeline on first use."""
    global _chain
    if _chain is None:
        # Imported lazily so the app imports without the LLM dependencies loaded.
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_groq import ChatGroq

        if not config.GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Add it to your environment or .env file."
            )

        llm = ChatGroq(
            model_name=config.MODEL_NAME,
            api_key=config.GROQ_API_KEY,
            temperature=config.TEMPERATURE,
        )
        prompt = ChatPromptTemplate.from_messages(
            [("system", SYSTEM_PROMPT), ("user", "{input}")]
        )
        _chain = prompt | llm | StrOutputParser()
    return _chain


def generate_answer(question: str) -> str:
    """Return the chatbot's answer to a question."""
    chain = get_chain()
    return chain.invoke({"input": question})
