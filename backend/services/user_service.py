from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from uuid import UUID
from sqlalchemy.orm import selectinload

from ..models import User
from ..schemas.user import UserCreate, UserRead
from ..config import settings
from ..tasks import send_email_task

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """
    Service class for user-related operations.
    """

    @staticmethod
    async def create_user(db: AsyncSession, user_create: UserCreate) -> UserRead:
        """
        Register a new user.
        """
        hashed_password = pwd_context.hash(user_create.password)
        new_user = User(email=user_create.email, password_hash=hashed_password, role=user_create.role)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        send_email_task.delay(new_user.email, 'Welcome to Badminton Tournament Hub')
        return UserRead.from_orm(new_user)

    @staticmethod
    async def authenticate_user(db: AsyncSession, email: str, password: str) -> User: