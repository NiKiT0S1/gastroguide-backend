from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.ai import AIRequest, AIResponse
from app.services.ai_service import generate_ai_response
from app.core.database import get_db

router = APIRouter(prefix="/api/v1/ai", tags=["AI"])


@router.post("/chat", response_model=AIResponse)
def chat_ai(request: AIRequest, db: Session = Depends(get_db)):

    answer = generate_ai_response(request.message, db)

    return {"response": answer}