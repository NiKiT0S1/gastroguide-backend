from pydantic import BaseModel


class OfferResponse(BaseModel):
    id: int
    restaurant_id: int
    title: str
    description: str
    discount: str
    expires: str
    emoji: str
    color: str

    class Config:
        from_attributes = True