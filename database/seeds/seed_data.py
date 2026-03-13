import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random
import uuid

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/badminton_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

roles = ['admin', 'player', 'organizer']

async def seed_users(session):
    users = [
        {"id": uuid.uuid4(), "email": "admin@example.com", "password_hash": "hashedpassword1", "role": "admin"},
        {"id": uuid.uuid4(), "email": "player1@example.com", "password_hash": "hashedpassword2", "role": "player"},
        {"id": uuid.uuid4(), "email": "organizer1@example.com", "password_hash": "hashedpassword3", "role": "organizer"},
    ]
    for user in users:
        user['created_at'] = datetime.now() - timedelta(days=random.randint(1, 30))
        user['updated_at'] = user['created_at']
    await session.execute(
        """
        INSERT INTO users (id, email, password_hash, role, created_at, updated_at)
        VALUES (:id, :email, :password_hash, :role, :created_at, :updated_at)
        """,
        users
    )

async def seed_tournaments(session):
    tournaments = [
        {"id": uuid.uuid4(), "name": f"Tournament {i}", "location": "Location {i}",
         "start_date": datetime.now().date() - timedelta(days=random.randint(1, 30)),
         "end_date": datetime.now().date() + timedelta(days=random.randint(1, 10)),
         "participant_limit": random.randint(10, 50)}
        for i in range(1, 6)
    ]
    for tournament in tournaments:
        tournament['created_at'] = datetime.now() - timedelta(days=random.randint(1, 30))
        tournament['updated_at'] = tournament['created_at']
    await session.execute(
        """
        INSERT INTO tournaments (id, name, location, start_date, end_date, participant_limit, created_at, updated_at)
        VALUES (:id, :name, :location, :start_date, :end_date, :participant_limit, :created_at, :updated_at)
        """,
        tournaments
    )

async def seed_matches(session):
    matches = [
        {"id": uuid.uuid4(), "tournament_id": str(uuid.uuid4()), "player1_id": str(uuid.uuid4()),
         "player2_id": str(uuid.uuid4()), "scheduled_time": datetime.now() - timedelta(days=random.randint(1, 30)),
         "player1_score": random.randint(0, 21), "player2_score": random.randint(0, 21),
         "status": random.choice(['scheduled', 'completed', 'cancelled'])}
        for _ in range(10)
    ]
    for match in matches:
        match['created_at'] = datetime.now() - timedelta(days=random.randint(1, 30))
        match['updated_at'] = match['created_at']
    await session.execute(
        """
        INSERT INTO matches (id, tournament_id, player1_id, player2_id, scheduled_time, player1_score, player2_score, status, created_at, updated_at)
        VALUES (:id, :tournament_id, :player1_id, :player2_id, :scheduled_time, :player1_score, :player2_score, :status, :created_at, :updated_at)
        """,
        matches
    )

async def main():
    async with SessionLocal() as session:
        await seed_users(session)
        await seed_tournaments(session)
        await seed_matches(session)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(main())