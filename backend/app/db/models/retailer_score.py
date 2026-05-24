from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, JSON, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class RetailerScore(Base):
    __tablename__ = 'retailer_scores'

    id = Column(Integer, primary_key=True, index=True)
    retailer_id = Column(Integer, ForeignKey('retailers.id', ondelete='CASCADE'))
    score = Column(Float, nullable=False, default=0.0)
    rank = Column(String, nullable=True)
    inputs = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    retailer = relationship('Retailer', back_populates='scores')
