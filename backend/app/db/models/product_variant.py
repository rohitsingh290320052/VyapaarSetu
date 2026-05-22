from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class ProductVariant(Base):
    __tablename__ = 'product_variants'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    moq = Column(Integer, nullable=False, default=1)
    stock_estimate = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship('Product', back_populates='variants')
