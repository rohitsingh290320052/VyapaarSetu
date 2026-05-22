from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.dependencies import get_current_active_user, get_db
from app.schemas.group_order import GroupOrderCreate, GroupOrderRead
from app.services.group_order_service import create_group_order
from app.db.models.group_order import GroupOrder

router = APIRouter()


@router.post('/', response_model=GroupOrderRead)
async def create_group_order_endpoint(
    payload: GroupOrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_active_user),
):
    if current_user.role not in ('brand', 'admin'):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Only brands or admins can create campaigns')
    group_order = await create_group_order(db, payload.model_dump())
    return group_order


@router.get('/', response_model=list[GroupOrderRead])
async def list_group_orders(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_active_user),
):
    result = await db.execute(select(GroupOrder).where(GroupOrder.status == 'open'))
    return result.scalars().all()
