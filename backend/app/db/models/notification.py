from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    channel = Column(String, nullable=False, default='app')
    payload = Column(JSON, nullable=True)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')
