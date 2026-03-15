# Pydantic-схемы ответа маршрута:
# distance, duration, coordinates.

from pydantic import BaseModel


class RouteResponse(BaseModel):
    distance: float
    duration: float
    geometry: list[list[float]]