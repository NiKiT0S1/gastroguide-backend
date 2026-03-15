import google.generativeai as genai
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem
from app.models.offer import Offer


genai.configure(api_key=settings.gemini_api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def build_restaurants_context(restaurants, menu_items, offers):
    text = ""

    for r in restaurants:
        text += f"""
Restaurant: {r.name}
Type: {r.type}
Rating: {r.rating}
Distance: {r.dist}
Address: {r.address}
Description: {r.description}
"""

        restaurant_menu = [m for m in menu_items if m.restaurant_id == r.id]

        if restaurant_menu:
            text += "Menu:\n"
            for item in restaurant_menu:
                text += f"- {item.name}: {item.price}\n"

        restaurant_offers = [o for o in offers if o.restaurant_id == r.id]

        if restaurant_offers:
            text += "Offers:\n"
            for offer in restaurant_offers:
                text += f"- {offer.title}: {offer.description}\n"

        text += "\n"

    return text

def build_history_context(history):
    if not history:
        return ""

    lines = []
    for msg in history[-10:]:
        role = "User" if msg.role == "user" else "Assistant"
        lines.append(f"{role}: {msg.text}")

    return "\n".join(lines)

def generate_ai_response(message: str, history: list, db: Session):
    restaurants = db.query(Restaurant).all()
    menu_items = db.query(MenuItem).all()
    offers = db.query(Offer).all()

    restaurants_context = build_restaurants_context(restaurants, menu_items, offers)
    history_context = build_history_context(history)

    prompt = f"""
You are GastroGuide AI assistant for restaurant recommendations in Astana.

Available restaurants:

{restaurants_context}

Previous conversation:
{history_context}

User question:
{message}

Rules:
- Recommend only from available data
- Consider menu and offers
- Answer naturally and briefly
"""

    response = model.generate_content(prompt)

    return response.text