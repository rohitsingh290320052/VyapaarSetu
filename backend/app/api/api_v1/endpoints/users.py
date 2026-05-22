from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_active_user, get_db
from app.schemas.user import UserRead
from app.db.models.user import User

router = APIRouter()


@router.get('/me', response_model=UserRead)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user
