from pydantic import BaseModel

class DraftRequest(BaseModel):
    topic: str
    tone: str = "neutral"

class DraftResponse(BaseModel):
    draft: str
