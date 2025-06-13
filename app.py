from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):
    return {"answer": f"You asked: {data.question}"}
