from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    configuration = Column(JSON, nullable=True)
    performance = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    brand = relationship('Brand', back_populates='campaigns')
