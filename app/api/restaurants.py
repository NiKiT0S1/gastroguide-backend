# REST endpoints для работы с заведениями:
# получение списка заведений,
# получение конкретного заведения по id.

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import or_

from app.core.database import get_db
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantResponse, MenuItemResponse
from app.models.menu_item import MenuItem
from app.models.offer import Offer
from app.services.location_service import haversine_distance

###############---Coordination Logic Without PostGIS---###############
import math

def calculate_distance(lat1, lng1, lat2, lng2):
    return math.sqrt((lat1 - lat2) ** 2 + (lng1 - lng2) ** 2) * 111000
######################################################################

router = APIRouter(prefix="/api/v1/restaurants", tags=["Restaurants"])

@router.get("", response_model=list[RestaurantResponse])
def get_restaurants(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Restaurant)

    if category_id is not None:
        query = query.filter(Restaurant.category_id == category_id)

    restaurants = query.all()
    return restaurants

@router.get("/search", response_model=list[RestaurantResponse])
def search_restaurants(q: str, db: Session = Depends(get_db)):
    restaurants = (
        db.query(Restaurant)
        .options(selectinload(Restaurant.menu))
        .filter(
            or_(
                Restaurant.name.ilike(f"%{q}%"),
                Restaurant.type.ilike(f"%{q}%"),
                Restaurant.description.ilike(f"%{q}%")
            )
        )
        .all()
    )
    return restaurants

######################################################################
@router.get("/nearby", response_model=list[RestaurantResponse])
def get_nearby_restaurants(
    lat: float = Query(...),
    lng: float = Query(...),
    radius: int = Query(1000, ge=1),
    db: Session = Depends(get_db),
):
    restaurants = db.query(Restaurant).all()

    nearby_restaurants = []

    for restaurant in restaurants:
        if restaurant.lat is None or restaurant.lng is None:
            continue

        distance_m = haversine_distance(lat, lng, restaurant.lat, restaurant.lng)

        if distance_m <= radius:
            nearby_restaurants.append((restaurant, distance_m))

    nearby_restaurants.sort(key=lambda item: item[1])

    return [restaurant for restaurant, _ in nearby_restaurants]
######################################################################

@router.get("/{restaurant_id}/menu", response_model=list[MenuItemResponse])
def get_restaurant_menu(restaurant_id: int, db: Session = Depends(get_db)):
    menu = db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()
    return menu

@router.get("/{restaurant_id}/offer")
def get_restaurant_offer(restaurant_id: int, db: Session = Depends(get_db)):
    offers = db.query(Offer).filter(Offer.restaurant_id == restaurant_id).all()
    return offers

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant_by_id(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = (
        db.query(Restaurant)
        .options(selectinload(Restaurant.menu))
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return restaurant
