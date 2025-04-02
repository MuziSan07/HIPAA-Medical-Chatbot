from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI(title="HIPAA-Compliant Medical Chatbot", version="1.1")

# CORS Middleware (Allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM with the requested model
llm = ChatGroq(
    model_name="llama-3.2-90b-vision-preview",  # Updated model
    api_key=GROQ_API_KEY,
    temperature=0.1  # Low temperature for factual responses
)

# Request model
class ChatRequest(BaseModel):
    question: str

# Define structured prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a HIPAA-compliant medical chatbot. Provide medically accurate, reliable, and secure responses.
    Do not diagnose patients or store personal health information (PHI). Follow HIPAA guidelines strictly."""),  
    ("user", "{input}")
])

# Create chatbot response chain
chain = prompt | llm | StrOutputParser()

# API Endpoint for chatbot
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        result = chain.invoke({"input": request.question})
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve static frontend (Bootstrap UI)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

# Run FastAPI (Development mode)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
