import uuid
from sqlalchemy import Column, String, Integer, Date, ForeignKey, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    """User model."""
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default='player')  # Ensure role is one of 'admin', 'organizer', 'player', 'umpire'
    created_at = Column(TIMESTAMP, server_default=text('NOW()'), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=text('NOW()'), onupdate=text('NOW()'), nullable=False)

    def __init__(self, email, password_hash, role='player'):
        self.email = email
        self.password_hash = password_hash
        if role not in ['admin', 'organizer', 'player', 'umpire']:
            raise ValueError("Invalid user role")
        self.role = role


class Tournament(Base):
    """Tournament model."""
    __tablename__ = 'tournaments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    participant_limit = Column(Integer, nullable=False)