# test_models.py
import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import User, Tournament, Match

@pytest.mark.asyncio
async def test_user_model_constraints(override_get_db):
    """Test user model constraints and uniqueness."""
    async with override_get_db() as db:
        user = User(email="test@example.com", password_hash="hashed_password", role="user")
        db.add(user)
        await db.commit()
        with pytest.raises(IntegrityError):
            duplicate_user = User(email="test@example.com", password_hash="another_hash", role="user")
            db.add(duplicate_user)
            await db.commit()

@pytest.mark.asyncio
async def test_tournament_model(override_get_db):
    """Test tournament model creation."""
    async with override_get_db() as db:
        tournament = Tournament(name="Test Tournament", location="Test Location", start_date="2023-11-01", end_date="2023-11-05", participant_limit=16)
        db.add(tournament)
        await db.commit()
        assert tournament.id is not None

@pytest.mark.asyncio
async def test_match_model_relations(override_get_db):
    """Test match model relationships with users and tournaments."""
    async with override_get_db() as db:
        user1 = User(email="player1@example.com", password_hash="hashed_password1", role="player")
        user2 = User(email="player2@example.com", password_hash="hashed_password2", role="player")
        tournament = Tournament(name="Match Tournament", location="Arena", start_date="2023-11-01", end_date="2023-11-05", participant_limit=16)
        db.add_all([user1, user2, tournament])
        await db.commit()

        match = Match(tournament_id=tournament.id, player1_id=user1.id, player2_id=user2.id, scheduled_time="2023-11-01T10:00:00")
        db.add(match)
        await db.commit()
        assert match.id is not None