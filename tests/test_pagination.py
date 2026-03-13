# test_pagination.py
import pytest

@pytest.mark.asyncio
async def test_tournament_pagination(async_client, token_headers):
    """Test tournament listing with pagination."""
    # Create multiple tournaments
    for i in range(20):
        await async_client.post(
            "/api/v1/tournaments",
            headers=token_headers,
            json={"name": f"Tournament {i}", "location": "Location", "start_date": "2023-11-01", "end_date": "2023-11-05", "participant_limit": 16}
        )

    # Test pagination
    response = await async_client.get("/api/v1/tournaments?page=1&limit=10", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10

    response = await async_client.get("/api/v1/tournaments?page=2&limit=10", headers=token_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10