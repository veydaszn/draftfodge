from fastapi import FastAPI
from app.schemas import DraftRequest, DraftResponse
from app.writer import generate_draft

app = FastAPI(
    title="DraftFodge API",
    description="AI-powered writing and outline generator",
    version="1.0"
)

@app.post("/generate", response_model=DraftResponse)
def generate(request: DraftRequest):
    draft = generate_draft(request.topic, request.tone)
    return DraftResponse(draft=draft)
