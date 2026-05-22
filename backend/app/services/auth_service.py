from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from app.db.models.user import User
from app.core.security import create_access_token, create_refresh_token

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def authenticate_user(db: AsyncSession, identifier: str, password: str) -> User | None:
    stmt = select(User).where(or_(User.email == identifier, User.phone == identifier))
    result = await db.execute(stmt)
    user = result.scalars().first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_tokens_for_user(user: User) -> dict[str, str]:
    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))
    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}
