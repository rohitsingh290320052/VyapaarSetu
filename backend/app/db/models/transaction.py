from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey('payments.id', ondelete='SET NULL'))
    retailer_id = Column(Integer, ForeignKey('retailers.id', ondelete='SET NULL'))
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String, nullable=False, default='INR')
    type = Column(String, nullable=False)
    status = Column(String, nullable=False, default='completed')
    meta = Column('metadata', JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    payment = relationship('Payment')
    retailer = relationship('Retailer')
