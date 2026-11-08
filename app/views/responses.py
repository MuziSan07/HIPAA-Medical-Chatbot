"""Response formatting (View layer).

Keeps presentation concerns — such as attaching the standing medical disclaimer
— out of the controllers and the domain model.
"""

from ..models.schemas import ChatResponse

DISCLAIMER = (
    "This chatbot provides general educational information only and is not a "
    "substitute for professional medical advice, diagnosis, or treatment. "
    "Do not enter real personal health information. Always consult a qualified "
    "healthcare provider with any medical questions."
)


def build_chat_response(answer: str) -> ChatResponse:
    """Wrap a model answer in the API response shape, with the disclaimer."""
    return ChatResponse(response=answer, disclaimer=DISCLAIMER)
