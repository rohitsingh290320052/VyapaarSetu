from pydantic import BaseSettings, AnyHttpUrl, PostgresDsn, field_validator
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = 'RetailLink'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000']
    DATABASE_URL: PostgresDsn
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = '.env.example'
        case_sensitive = True

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    def split_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(',') if i.strip()]
        return v

settings = Settings()
