from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.dependencies import get_db
from app.schemas.auth import TokenRequest, RegistrationRequest
from app.schemas.token import Token
from app.schemas.user import UserRead
from app.services.auth_service import authenticate_user, create_tokens_for_user, get_password_hash
from app.db.models.user import User

router = APIRouter()


@router.post('/register', response_model=UserRead)
async def register_user(payload: RegistrationRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalars().first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')

    user = User(
        email=payload.email,
        phone=payload.phone,
        hashed_password=get_password_hash(payload.password),
        role=payload.role,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.post('/token', response_model=Token)
async def login_for_access_token(payload: TokenRequest, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    return create_tokens_for_user(user)
