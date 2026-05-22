from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class OrderParticipant(Base):
    __tablename__ = 'order_participants'

    id = Column(Integer, primary_key=True, index=True)
    group_order_id = Column(Integer, ForeignKey('group_orders.id', ondelete='CASCADE'))
    retailer_id = Column(Integer, ForeignKey('retailers.id', ondelete='CASCADE'))
    quantity = Column(Integer, nullable=False)
    committed_price = Column(Numeric(12, 2), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False, default='confirmed')

    group_order = relationship('GroupOrder', back_populates='participants')
    retailer = relationship('Retailer')
