**HIPAA-Compliant Medical Chatbot**


**Description**

This project is a HIPAA-compliant medical chatbot that leverages the power of LangChain and Groq API to provide accurate and secure medical-related information. It ensures that personal health information (PHI) is not stored or mishandled, complying with HIPAA guidelines.

The backend is built using FastAPI, and the frontend is a responsive Bootstrap-based UI that allows users to interact with the chatbot by typing in their medical questions.


**Features:**

HIPAA Compliance: Provides medically accurate responses while ensuring the privacy and security of PHI.

User Interaction: Users can type their questions and receive responses based on the latest medical guidelines.

Frontend: A modern, responsive chat interface built with HTML, CSS, Bootstrap, and jQuery.

Backend: A FastAPI-based backend that uses the Groq API for medical responses, ensuring accuracy and security.


**Tech Stack**

*Frontend*:

HTML

CSS (Bootstrap)

JavaScript (jQuery)

*Backend:*

Python (FastAPI)

LangChain (for GPT-powered chat)

Groq API (for the model used in the chatbot)

Uvicorn (ASGI server)


*Other:*

Dotenv for environment variables

CORS Middleware for frontend-backend communication

Static Files for serving frontend resources


**Requirements**

Python 3.7+

Install required dependencies with the following command:

```python
pip install -r requirements.txt
```

*Frontend:*
Requires Bootstrap and jQuery which are loaded from CDNs.

*Environment Variables:*
Create a .env file with the following content:

```python
GROQ_API_KEY=your_groq_api_key
```

Replace your_groq_api_key with your actual Groq API key.


**Running the Application**

*Backend:*

Install dependencies:
```python
pip install -r requirements.txt
```

Run the FastAPI server:
```python
uvicorn medical-chatbot:app --reload
```

This will start the FastAPI server at http://127.0.0.1:8000/.


*Frontend:*
The frontend files are served from the /static directory in the FastAPI app.

Navigate to http://127.0.0.1:8000/ in your browser to access the chatbot interface.

**API Endpoints**

*POST /chat:*
Request body:

```json
{
  "question": "Your medical question here"
}
```

Response body:

```json
{
  "response": "The chatbot's response to your question"
}
```

Structure of the Application
```
├── backend/
│   ├── main.py              # FastAPI app with route and chatbot logic
│   ├── .env                 # Environment variables (GROQ_API_KEY)
│   ├── requirements.txt     # Python dependencies
│   └── static/              # Frontend static files (HTML, CSS, JS)
│       └── index.html       # Frontend chat UI
├── frontend/                # Frontend files (included in 'static' folder)
└── README.md                # Project Documentation
```

**Frontend Overview**
The frontend contains a simple chat interface that allows users to enter medical questions. Responses from the bot are displayed in the chat window, with each message from the user and bot styled accordingly. The interface is designed to be user-friendly and mobile-responsive.

The chat interface allows users to:

Enter their questions in a text box.

View responses from the chatbot.

Have the chat window scroll automatically as new messages appear.

**Security and Privacy**
The chatbot adheres to HIPAA guidelines.

Personal health information (PHI) is not stored or processed. Only the input question is passed to the chatbot, and no personal details are retained.

Responses are generated based on publicly available medical knowledge and are not intended for medical diagnosis or treatment.

**Troubleshooting**
Error: Unable to get a response.
If you encounter an error stating that the response could not be fetched, ensure that your Groq API key is correct and that your server is running correctly.

*CORS issues:*
If the frontend cannot communicate with the backend, make sure that the CORS middleware is correctly set up in your FastAPI app.

**License**
This project is open-source and available under the MIT License.



