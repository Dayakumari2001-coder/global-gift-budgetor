"""config.py - Application configuration settings loaded from environment variables."""

from pydantic import BaseModel, ConfigDict

#database connection settings
class Settings(BaseModel):
    """Application settings loaded from environment variables."""

    # Database
    DB_HOST: str = "127.0.0.1"
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_NAME: str= "gift_db"

    # Exchange Rate API
    EXCHANGE_RATE_API_KEY: str = ""
    EXCHANGE_RATE_BASE_URL: str = "https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}"

    model_config = ConfigDict(env_file = ".env",case_sensitive = True)

settings = Settings()
