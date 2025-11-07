from fastapi import FastAPI

from .llm import LLM

app = FastAPI()

llm = LLM()

@app.get("/")
def health_check():
    return {"message": "Hello, World!"}

@app.get("/chat/{query}")
def chat(query: str):
    response = llm.chat(query)
    return {"response": response}