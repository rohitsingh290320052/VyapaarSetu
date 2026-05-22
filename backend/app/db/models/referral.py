from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Referral(Base):
    __tablename__ = 'referrals'

    id = Column(Integer, primary_key=True, index=True)
    retailer_id = Column(Integer, ForeignKey('retailers.id', ondelete='CASCADE'))
    referred_phone = Column(String, nullable=False)
    status = Column(String, nullable=False, default='pending')
    reward_earned = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    retailer = relationship('Retailer', back_populates='referrals')
