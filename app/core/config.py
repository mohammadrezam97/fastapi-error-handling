# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Enterprise Error Handling"
    debug: bool = True

settings = Settings()
