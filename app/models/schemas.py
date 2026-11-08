"""Request and response data models (the Model layer's schemas)."""

from pydantic import BaseModel, Field

from .. import config


class ChatRequest(BaseModel):
    """A single chatbot question."""

    question: str = Field(
        ...,
        min_length=1,
        max_length=config.MAX_QUESTION_LENGTH,
        description="The user's medical question (no personal health information).",
    )


class ChatResponse(BaseModel):
    """The chatbot's answer plus a standing disclaimer."""

    response: str
    disclaimer: str
