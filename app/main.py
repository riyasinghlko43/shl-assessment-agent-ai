from fastapi import FastAPI

from app.schemas import ChatRequest

from app.agent import generate_response

app = FastAPI()


@app.get("/health")
def health():

    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(
        [msg.dict() for msg in request.messages]
    )

    return response