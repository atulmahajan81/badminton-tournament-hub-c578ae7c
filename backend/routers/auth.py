from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from backend.auth import create_access_token, create_refresh_token, get_password_hash, verify_password
from backend.dependencies import get_db_session
from backend.models import User
from backend.schemas import UserCreate, UserOut, TokenOut
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.middleware import Middleware

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

limiter = Limiter(key_func=get_remote_address)

@limiter.limit("5/minute")
@router.post("/register", response_model=UserOut)
async def register(user_create: UserCreate, session: AsyncSession = Depends(get_db_session)) -> UserOut:
    """Register a new user."""
    if not validate_password(user_create.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password does not meet complexity requirements.")
    statement = select(User).options(selectinload(User.roles)).where(User.email == user_create.email)
    result = await session.execute(statement)
    if result.scalars().first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    hashed_password = get_password_hash(user_create.password)
    new_user = User(email=user_create.email, password_hash=hashed_password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@limiter.limit("5/minute")
@router.post("/login", response_model=TokenOut)
async def login(user_create: UserCreate, session: AsyncSession = Depends(get_db_session)) -> TokenOut:
    """Login user and return token."""
    statement = select(User).where(User.email == user_create.email)
    result = await session.execute(statement)
    user = result.scalars().first()
    if not user or not verify_password(user_create.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=15))
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    return TokenOut(access_token=access_token, token_type="bearer")