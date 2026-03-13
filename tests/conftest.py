# conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app
from backend.database import Base, get_db

# Create an in-memory SQLite database for testing
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture(scope='function', autouse=True)
async def override_get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def token_headers(async_client):
    # Mock user registration and login to get a token
    registration_data = {"email": "test@example.com", "password": "password", "role": "user"}
    await async_client.post("/api/v1/auth/register", json=registration_data)
    login_data = {"email": "test@example.com", "password": "password"}
    response = await async_client.post("/api/v1/auth/login", json=login_data)
    data = response.json()
    return {"Authorization": f"Bearer {data['access_token']}"}

# Mock external services
@pytest.fixture
def mock_external_services():
    with patch('backend.services.email_service.send_email') as mock_send_email:
        yield mock_send_email