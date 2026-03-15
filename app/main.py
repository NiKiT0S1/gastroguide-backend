from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.core.config import settings
from app.core.database import Base, engine
from app.models import Restaurant
from app.api.restaurants import router as restaurants_router
from app.api.offers import router as offers_router
from app.api.ai import router as ai_router
from app.api.routes import router as routes_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(restaurants_router)
app.include_router(offers_router)
app.include_router(ai_router)
app.include_router(routes_router)


@app.get("/")
async def root():
    return {"message": "GastroGuide Backend is running"}


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database_configured": bool(settings.database_url)
    }


@app.get("/db-check")
async def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}