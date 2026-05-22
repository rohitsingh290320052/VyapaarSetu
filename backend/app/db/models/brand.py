from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    company_name = Column(String, nullable=False)
    gst_number = Column(String, nullable=True)
    website = Column(String, nullable=True)
    moq_default = Column(Integer, nullable=False, default=50)
    catalog_metadata = Column(JSON, nullable=True)
    approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship('User', back_populates='brand_profile')
    products = relationship('Product', back_populates='brand')
    campaigns = relationship('Campaign', back_populates='brand')
