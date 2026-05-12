"""config.py - Application configuration settings loaded from environment variables."""
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict

#database connection settings
class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    DB_HOST: ClassVar[str] = "127.0.0.1"
    DB_USER: ClassVar[str]= "root"
    DB_PASSWORD: ClassVar[str] = ""
    DB_NAME: ClassVar[str]= "gift_db"

    # Exchange Rate API
    EXCHANGE_RATE_API_KEY: str = ""
    EXCHANGE_RATE_BASE_URL: str = "https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}"

    Model_Config =SettingsConfigDict(
        env_file = "../../.env",
        case_sensitive = True
    )

settings = Settings()
