from pydantic import BaseModel, EmailStr
from typing import Optional


class TokenRequest(BaseModel):
    username: str
    password: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RegistrationRequest(BaseModel):
    email: EmailStr
    phone: Optional[str]
    password: str
    role: str
