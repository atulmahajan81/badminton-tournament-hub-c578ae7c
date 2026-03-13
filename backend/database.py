from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from contextlib import asynccontextmanager

from .config import Settings

settings = Settings()

# Create Async SQLAlchemy engine
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True, pool_size=10, max_overflow=20, pool_timeout=30)  # Set echo to False for production

# Create a configured "Session" class
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for our models
Base: DeclarativeMeta = declarative_base()

@asynccontextmanager
def get_db() -> AsyncSession:
    """Dependency to provide database session."""
    async with AsyncSessionLocal() as session:
        yield session