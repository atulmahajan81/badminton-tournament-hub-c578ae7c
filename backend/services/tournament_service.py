from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List
from ..cache import redis_cache

from ..models import Tournament
from ..schemas.tournament import TournamentCreate, TournamentRead, TournamentUpdate


class TournamentService:
    """
    Service class for tournament-related operations.
    """

    @staticmethod
    @redis_cache(ttl=300)
    async def list_tournaments(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[TournamentRead]:
        """
        List tournaments with pagination.
        """
        result = await db.execute(select(Tournament).options(selectinload(Tournament.matches)).offset(skip).limit(limit))
        tournaments = result.scalars().all()
        return [TournamentRead.from_orm(t) for t in tournaments]

    @staticmethod
    async def create_tournament(db: AsyncSession, tournament_create: TournamentCreate, current_user: dict) -> TournamentRead:
        """
        Create a new tournament.
        """
        tournament = Tournament(**tournament_create.dict(), organizer_id=current_user['id'])
        db.add(tournament)
        await