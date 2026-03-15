# Конфигурация приложения.
# Файл загружает переменные окружения из .env
# и предоставляет их для использования в проекте.

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    gemini_api_key: str
    ors_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()