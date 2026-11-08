"""Application factory and entry point.

Run with::

    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from . import config
from .controllers.chat_controller import router as chat_router


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    app = FastAPI(title="HIPAA-Aware Medical Chatbot", version="1.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount(
        "/static",
        StaticFiles(directory=str(config.STATIC_DIR)),
        name="static",
    )

    app.include_router(chat_router)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
