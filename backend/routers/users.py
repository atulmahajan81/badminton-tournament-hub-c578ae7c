from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.dependencies import get_db_session, get_current_user, get_current_admin, pagination_params
from backend.models import User
from backend.schemas import UserOut, UserUpdate

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
async def list_users(session: AsyncSession = Depends(get_db_session), pagination: dict = Depends(pagination_params)) -> list[UserOut]:
    """List users with pagination."""
    statement = select(User).offset(pagination['skip']).limit(pagination['limit'])
    result = await session.execute(statement)
    users = result.scalars().all()
    return [UserOut(id=user.id, email=user.email, created_at=user.created_at) for user in users]

@router.get("/{id}", response_model=UserOut)
async def get_user(id: str, session: AsyncSession = Depends(get_db_session)) -> UserOut:
    """Get a user by ID."""
    statement = select(User).where(User.id == id)
    result = await session.execute(statement)
    user = result.scalars().first()
    if user is None:
        rai