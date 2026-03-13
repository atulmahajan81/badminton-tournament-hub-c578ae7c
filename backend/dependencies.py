from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import User
from backend.auth import verify_token

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_db_session() -> AsyncSession:
    """Dependency that provides a database session."""
    async with async_sessionmaker() as session:
        yield session

async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_db_session)) -> User:
    """Get the current user from the token."""
    try:
        payload = verify_token(token)
        user_id: str = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        statement = select(User).where(User.id == user_id)
        result = await session.execute(statement)
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

async def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    """Ensure the current user is an admin."""
    if current_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return current_user

async def pagination_params(page: int = 1, size: int = 10):
    """Pagination parameters."""
    return page, size