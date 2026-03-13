# test_auth.py
import pytest

@pytest.mark.asyncio
async def test_register_user(async_client):
    """Test user registration with valid data."""
    response = await async_client.post("/api/v1/auth/register", json={"email": "newuser@example.com", "password": "newpassword", "role": "user"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "newuser@example.com"

@pytest.mark.asyncio
async def test_register_user_missing_fields(async_client):
    """Test registration with missing fields."""
    response = await async_client.post("/api/v1/auth/register", json={"email": "", "password": ""})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_login_user(async_client):
    """Test user login."""
    response = await async_client.post("/api/v1/auth/login", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

@pytest.mark.asyncio
async def test_login_user_invalid_credentials(async_client):
    """Test login with invalid credentials."""
    response = await async_client.post("/api/v1/auth/login", json={"email": "wrong@example.com", "password": "wrongpassword"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_refresh_token(async_client, token_headers):
    """Test token refresh with valid refresh token."""
    response = await async_client.post("/api/v1/auth/refresh", headers=token_headers, json={"refresh_token": "valid_refresh_token"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

@pytest.mark.asyncio
async def test_logout(async_client, token_headers):
    """Test user logout."""
    response = await async_client.post("/api/v1/auth/logout", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Successfully logged out"