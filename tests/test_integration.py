# test_integration.py
import pytest

@pytest.mark.asyncio
async def test_full_integration_flow(async_client):
    """Test full integration flow from registration to tournament creation."""
    # Register a user
    registration_response = await async_client.post("/api/v1/auth/register", json={"email": "flow@example.com", "password": "flowpass", "role": "user"})
    assert registration_response.status_code == 201
    user_data = registration_response.json()

    # Login
    login_response = await async_client.post("/api/v1/auth/login", json={"email": "flow@example.com", "password": "flowpass"})
    assert login_response.status_code == 200
    token_data = login_response.json()
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}

    # Create a tournament
    tournament_response = await async_client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Flow Tournament", "location": "Flow Arena", "start_date": "2023-11-01", "end_date": "2023-11-05", "participant_limit": 16}
    )
    assert tournament_response.status_code == 201
    tournament_data = tournament_response.json()

    # Get tournament details
    tournament_detail_response = await async_client.get(f"/api/v1/tournaments/{tournament_data['id']}", headers=headers)
    assert tournament_detail_response.status_code == 200

    # Update tournament
    update_response = await async_client.put(
        f"/api/v1/tournaments/{tournament_data['id']}",
        headers=headers,
        json={"name": "Updated Tournament", "location": "Updated Location"}
    )
    assert update_response.status_code == 200

    # Delete tournament
    delete_response = await async_client.delete(f"/api/v1/tournaments/{tournament_data['id']}", headers=headers)
    assert delete_response.status_code == 204