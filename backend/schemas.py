from pydantic import BaseModel, EmailStr, Field
from pydantic.config import ConfigDict
from uuid import UUID
from datetime import datetime, date

class TokenOut(BaseModel):
    """Schema for login token response."""
    access_token: str
    token_type: str = Field(default='bearer')

class UserOut(BaseModel):
    """Schema for user registration response."""
    id: UUID
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    """Schema for creating a user."""
    email: EmailStr
    password: str

class TournamentOut(BaseModel):
    """Schema for tournament response."""
    id: UUID
    name: str
    location: str
    start_date: date
    end_date: date
    participant_limit: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TournamentCreate(BaseModel):
    """Schema for creating a tournament."""
    name: str
    location: str
    start_date: date
    end_date: date
    participant_limit: int

class MatchOut(BaseModel):
    """Schema for match response."""
    id: UUID
    tournament_id: UUID
    player1_id: UUID
    player2_id: UUID
    scheduled_time: datetime
    player1_score: int | None
    player2_score: int | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class MatchCreate(BaseModel):
    """Schema for creating a match."""
    tournament_id: UUID
    player1_id: UUID
    player2_id: UUID
    scheduled_time: datetime