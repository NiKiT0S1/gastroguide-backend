from datetime import datetime
from pydantic import BaseModel


class MenuItemResponse(BaseModel):
    id: int
    restaurant_id: int
    name: str
    price: str
    emoji: str
    popular: bool

    class Config:
        from_attributes = True


class RestaurantResponse(BaseModel):
    id: int
    name: str
    type: str
    emoji: str
    color: str
    tag: str
    rating: float
    reviews: int
    dist: str
    time: str
    price: str
    open: bool
    address: str
    phone: str
    description: str
    hours: str
    lat: float
    lng: float
    features: list[str]
    photos: list[str]
    price_range: int
    created_at: datetime
    updated_at: datetime
    menu: list[MenuItemResponse] = []

    class Config:
        from_attributes = True