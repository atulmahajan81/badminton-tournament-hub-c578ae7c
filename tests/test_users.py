# test_users.py
import pytest

@pytest.mark.asyncio
async def test_get_current_user_profile(async_client, token_headers):
    """Test retrieving the current user's profile."""
    response = await async_client.get("/api/v1/users/me", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "email" in data
    assert "role" in data

@pytest.mark.asyncio
async def test_update_user_profile(async_client, token_headers):
    """Test updating the user's profile."""
    response = await async_client.put("/api/v1/users/me", headers=token_headers, json={"email": "updated@example.com", "password": "newpassword"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "updated@example.com"

@pytest.mark.asyncio
async def test_get_user_profile_unauthorized(async_client):
    """Test fetching user profile without authorization."""
    response = await async_client.get("/api/v1/users/me")
    assert response.status_code == 401