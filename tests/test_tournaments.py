# test_tournaments.py
import pytest

@pytest.mark.asyncio
async def test_create_tournament(async_client, token_headers):
    """Test creating a new tournament."""
    response = await async_client.post(
        "/api/v1/tournaments",
        headers=token_headers,
        json={
            "name": "Open Tournament",
            "location": "City Arena",
            "start_date": "2023-11-01",
            "end_date": "2023-11-05",
            "participant_limit": 16
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Open Tournament"

@pytest.mark.asyncio
async def test_list_tournaments(async_client, token_headers):
    """Test listing all tournaments."""
    response = await async_client.get("/api/v1/tournaments", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_get_tournament_details(async_client, token_headers):
    """Test getting tournament details by ID."""
    # Assume a tournament with ID '12345' exists
    response = await async_client.get("/api/v1/tournaments/12345", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data

@pytest.mark.asyncio
async def test_register_for_tournament(async_client, token_headers):
    """Test registering for a tournament."""
    # Assume a tournament with ID '12345' exists
    response = await async_client.post("/api/v1/tournaments/12345/register", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Registered successfully"