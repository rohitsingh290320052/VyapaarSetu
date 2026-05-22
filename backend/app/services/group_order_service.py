from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.group_order import GroupOrder


async def create_group_order(db: AsyncSession, payload: dict) -> GroupOrder:
    group_order = GroupOrder(
        title=payload['title'],
        description=payload.get('description'),
        pincode=payload['pincode'],
        category=payload.get('category'),
        geo_radius_meters=payload.get('geo_radius_meters'),
        moq_target=payload['moq_target'],
        product_variant_id=payload['product_variant_id'],
        brand_id=payload['brand_id'],
        pricing_tiers=payload.get('pricing_tiers', []),
        expires_at=payload.get('expires_at'),
    )
    db.add(group_order)
    await db.commit()
    await db.refresh(group_order)
    return group_order


async def increment_group_order(db: AsyncSession, group_order: GroupOrder, quantity: int) -> GroupOrder:
    group_order.current_quantity += quantity
    if group_order.current_quantity >= group_order.moq_target:
        group_order.status = 'completed'
    group_order.updated_at = datetime.utcnow()
    db.add(group_order)
    await db.commit()
    await db.refresh(group_order)
    return group_order
