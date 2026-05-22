from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class GroupOrderBase(BaseModel):
    title: str
    description: Optional[str]
    pincode: str
    moq_target: int
    category: Optional[str]
    geo_radius_meters: Optional[int]
    expires_at: Optional[datetime]
    pricing_tiers: Optional[List[dict]]


class GroupOrderCreate(GroupOrderBase):
    product_variant_id: int
    brand_id: int


class GroupOrderRead(GroupOrderBase):
    id: int
    current_quantity: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
