from pydantic import BaseModel


class RouteResponse(BaseModel):
    distance: float
    duration: float
    geometry: list[list[float]]