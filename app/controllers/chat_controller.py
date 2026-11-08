"""Chat controller — routes for the chatbot and the frontend page."""

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from .. import config
from ..models import chatbot_model
from ..models.schemas import ChatRequest, ChatResponse
from ..views.responses import build_chat_response

router = APIRouter()


@router.get("/")
async def serve_frontend():
    """Serve the chat UI."""
    return FileResponse(config.STATIC_DIR / "index.html")


@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest) -> ChatResponse:
    """Answer a medical question (validation handled by the ChatRequest model)."""
    try:
        answer = chatbot_model.generate_answer(request.question)
    except Exception as exc:  # noqa: BLE001 - surface chain/LLM errors as 500s
        raise HTTPException(status_code=500, detail=str(exc))
    return build_chat_response(answer)
