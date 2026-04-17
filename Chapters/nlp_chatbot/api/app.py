import pandas as pd
import uuid
from fastapi import FastAPI, Request
from pydantic import BaseModel
from etl.preprocess import clean_text
from model.vectorizer import build_vectorizer
from model.similarity import find_best_match
from services.memory_service import conversations_store
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services.memory_service import add_message, get_history

df = pd.read_csv("data/faq_data.csv")
df["clean_question"] = df["question"].apply(clean_text)
vectorizer, faq_vectors = build_vectorizer(df["clean_question"])


# faq_vectors = [
#   [0.71, 0.71, 0.0, 0.0, 0.0],   # FAQ 0
#   [0.0, 0.0, 0.71, 0.71, 0.0],   # FAQ 1
#   [0.0, 0.0, 0.0, 0.0, 1.0]      # FAQ 2
# ]

app = FastAPI(title="NLP Chatbot")
# sessions: Dict[str, List[str]] = {}

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class UserQuery(BaseModel):
    message: str
    session_id: str |None = None

class LoginRequest(BaseModel):
    username: str
    password: str

# print(df.head())

USERS = {
    "admin": "1234",
    "student": "abcd"
}

active_sessions = {}

@app.post("/login")
def login(user: LoginRequest):
    if user.username in USERS and USERS[user.username] == user.password:
        session_id = str(uuid.uuid4())
        active_sessions[session_id] = user.username

        return {
            "message": "Login successfully",
            "session_id": session_id,
            "username": user.username
        }
    return {
        "error": "Invalid username or password"
    }
@app.post("/chat")
def chat(user_input: UserQuery):

    # Create session if new user
    session_id = user_input.session_id 

    # Check Login
    if not session_id or session_id not in active_sessions:
        return {
            "error": "Unauthorized. Please login first."
        }
    username = active_sessions[session_id]

    clean_input = clean_text(user_input.message)  # clean_input = "provide placement assistance"
    user_vector = vectorizer.transform([clean_input])  # ['return', 'policy', 'placement', 'assistance', 'refund', 'order'] - > user_vector = [[0.0, 0.0, 0.71, 0.71, 0.0, 0.0]]

    # user_vector VS each row in faq_vectors
    # scores = [[0.05, 1.00, 0.00]]  -> best_index = 1 
    index, score = find_best_match(user_vector, faq_vectors)

    # Add user message to history
    add_message(session_id, "user", user_input.message)
    if score < 0.30:
        bot_response = "Sorry, I couldn't understand your question."
    else:
        bot_response = df.iloc[index]["answer"]

    # Add bot response to history
    add_message(session_id, "bot", bot_response)

    return {
        "username": username,
        "session_id": session_id,
        "response": bot_response,
        "confidence": round(float(score), 2),
        "history": get_history(session_id)
    }



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/debug/chats")
def view_all_chats():
    return conversations_store