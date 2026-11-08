"""HIPAA-aware medical chatbot — a FastAPI + LangChain/Groq application.

Package layout (Model-View-Controller):
    config                   Environment-driven settings.
    models.schemas           Request/response data models.
    models.chatbot_model     LangChain chain and response generation (domain).
    views.responses          Response formatting (View).
    views.static             Frontend chat UI (View).
    controllers.chat_controller  HTTP routes (Controller).
    main                     Application factory wiring the layers.
"""

__version__ = "1.1.0"
