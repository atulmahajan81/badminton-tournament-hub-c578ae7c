# test_services.py
import pytest
from unittest.mock import patch
from backend.services.user_service import create_user, authenticate_user

@pytest.mark.asyncio
async def test_create_user_service(override_get_db):
    """Test user creation service function."""
    async with override_get_db() as db:
        user = await create_user(db, email="service@example.com", password="password", role="user")
        assert user.email == "service@example.com"

@pytest.mark.asyncio
async def test_authenticate_user_service(override_get_db):
    """Test user authentication service function."""
    async with override_get_db() as db:
        await create_user(db, email="auth@example.com", password="password", role="user")
        user = await authenticate_user(db, email="auth@example.com", password="password")
        assert user is not None

@pytest.mark.asyncio
async def test_authenticate_user_invalid_service(override_get_db):
    """Test user authentication with invalid credentials."""
    async with override_get_db() as db:
        user = await authenticate_user(db, email="invalid@example.com", password="wrong")
        assert user is None