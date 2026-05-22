from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, String, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    order_participant_id = Column(Integer, ForeignKey('order_participants.id', ondelete='SET NULL'))
    retailer_id = Column(Integer, ForeignKey('retailers.id', ondelete='SET NULL'))
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String, nullable=False, default='INR')
    provider = Column(String, nullable=False, default='razorpay')
    provider_payload = Column(JSON, nullable=True)
    status = Column(String, nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    retailer = relationship('Retailer')
    participant = relationship('OrderParticipant')
