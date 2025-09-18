from fastapi import APIRouter
from pydantic import BaseModel
from main import main  

router = APIRouter()

class ChatRequest(BaseModel):
    key: str
    query: str

@router.post("/chatbot")
def ask_chatbot(chat: ChatRequest):
    response = main(chat.key, query=chat.query)
    return {"response": response}

