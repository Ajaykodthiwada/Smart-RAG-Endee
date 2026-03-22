from fastapi import FastAPI
from app.rag import search, load_data

app = FastAPI()

# Load initial data
load_data()

@app.get("/")
def home():
    return {"message": "Endee AI Project Running 🚀"}

@app.get("/ask")
def ask(q: str):
    results = search(q)
    return {
        "query": q,
        "results": results
    }