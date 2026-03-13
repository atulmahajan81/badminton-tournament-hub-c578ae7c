from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from ..services.tournament_service import TournamentService
from ..dependencies import get_db, get_current_user, pagination_params
from ..schemas.tournament import TournamentCreate, TournamentRead, TournamentUpdate

router = APIRouter(prefix="/api/v1/tournaments", tags=["Tournaments"])


@router.get("/", response_model=List[TournamentRead], response_model_exclude_unset=True)
async def list_tournaments(pagination: dict = Depends(pagination_params), db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    List all tournaments with pagination.
    """
    tournaments = await TournamentService.list_tournaments(db, skip=pagination['skip'], limit=pagination['limit'])
    return tournaments


@router.post("/", response_model=TournamentRead)
async def create_tournament(tournament: TournamentCreate, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Create a new tournament.
    """
    return await TournamentService.create_tournament(db, tournament, current_user)


@router.get("/{tournament_id}