
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "fastapi-assign"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./test.db"
    APP_VERSION: str = "0.0.1"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",  
    )

settings = Settings()
