from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='CASCADE'))
    name = Column(String, nullable=False, index=True)
    sku = Column(String, nullable=True, unique=True)
    category = Column(String, nullable=True, index=True)
    description = Column(String, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    brand = relationship('Brand', back_populates='products')
    variants = relationship('ProductVariant', back_populates='product')
