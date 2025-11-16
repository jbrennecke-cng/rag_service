from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
from app.rag_engine import answer_question
@app.get("/ask")
def ask(q: str):
    return {"answer": answer_question(q)}
