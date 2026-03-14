from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import google.api_core.exceptions

from app.schemas.ai import AIRequest, AIResponse
from app.services.ai_service import generate_ai_response
from app.core.database import get_db

router = APIRouter(prefix="/api/v1/ai", tags=["AI"])

@router.post("/chat", response_model=AIResponse)
def chat_ai(request: AIRequest, db: Session = Depends(get_db)):
    try:
        answer = generate_ai_response(request.message, db)
        return {"response": answer}
    except google.api_core.exceptions.GoogleAPIError as e:
        raise HTTPException(status_code=502, detail=f"Gemini API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal AI error: {str(e)}")