from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Retailer(Base):
    __tablename__ = 'retailers'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    shop_name = Column(String, nullable=False)
    gst_number = Column(String, nullable=True)
    pincode = Column(String, nullable=False, index=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    category = Column(String, nullable=True)
    shop_photo_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship('User', back_populates='retailer_profile')
    referrals = relationship('Referral', back_populates='retailer')
    scores = relationship('RetailerScore', back_populates='retailer')
