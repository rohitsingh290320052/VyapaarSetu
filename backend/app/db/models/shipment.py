from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    group_order_id = Column(Integer, ForeignKey('group_orders.id', ondelete='SET NULL'))
    carrier = Column(String, nullable=True)
    tracking_id = Column(String, nullable=True)
    status = Column(String, nullable=False, default='pending')
    route_cluster = Column(JSON, nullable=True)
    eta = Column(DateTime, nullable=True)
    meta = Column('metadata', JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    group_order = relationship('GroupOrder')
