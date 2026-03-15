# Pydantic-схемы для AI-чата.
# Описывают структуру:
# - входящего сообщения
# - истории диалога
# - исходящего AI-ответа

from pydantic import BaseModel, Field
from typing import Literal


class AIMessage(BaseModel):
    role: Literal["user", "ai"]
    text: str


class AIRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    history: list[AIMessage] = []


class AIResponse(BaseModel):
    response: str