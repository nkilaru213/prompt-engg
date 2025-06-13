from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS (important for frontend like React or Gradio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domain in production (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input schema
class QuestionRequest(BaseModel):
    question: str

# Example route for health check
@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running."}

# Main route to receive a prompt/question
@app.post("/ask")
def ask_question(payload: QuestionRequest):
    question = payload.question

    # Placeholder: Replace this logic with your LLM/vector search
    example_response = f"🤖 Echo: You asked - '{question}'"

    return {"answer": example_response}
