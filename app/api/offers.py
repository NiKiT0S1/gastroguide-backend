from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.offer import Offer
from app.schemas.offer import OfferResponse

router = APIRouter(prefix="/api/v1/offers", tags=["Offers"])


@router.get("", response_model=list[OfferResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(Offer).all()