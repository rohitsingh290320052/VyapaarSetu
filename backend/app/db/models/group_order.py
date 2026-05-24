from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean, JSON, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class GroupOrder(Base):
    __tablename__ = 'group_orders'

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='SET NULL'))
    product_variant_id = Column(Integer, ForeignKey('product_variants.id', ondelete='SET NULL'))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    pincode = Column(String, nullable=False, index=True)
    geo_radius_meters = Column(Integer, nullable=True)
    category = Column(String, nullable=True)
    moq_target = Column(Integer, nullable=False)
    current_quantity = Column(Integer, nullable=False, default=0)
    pricing_tiers = Column(JSON, nullable=True)
    status = Column(String, nullable=False, default='open')
    expires_at = Column(DateTime, nullable=True)
    meta = Column('metadata', JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    brand = relationship('Brand')
    product_variant = relationship('ProductVariant')
    participants = relationship('OrderParticipant', back_populates='group_order')
