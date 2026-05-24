from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, field_validator
from typing import List

env_path = Path('.') / '.env'
if not env_path.exists():
    load_dotenv(Path('.') / '.env.example')
else:
    load_dotenv(env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str = 'RetailLink'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000']
    # Allow using sqlite for local/dev runs (e.g. sqlite+aiosqlite:///./dev.db)
    DATABASE_URL: str = 'sqlite+aiosqlite:///./dev.db'
    # Development default secret — replace in production via env var
    JWT_SECRET_KEY: str = 'dev-secret'
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = '.env'
        case_sensitive = True

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    def split_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(',') if i.strip()]
        return v

settings = Settings()
