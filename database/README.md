# Badminton Tournament Hub Database

## Schema Description

The database schema is designed to support a Badminton Tournament Hub application with the following key entities:

- **Users**: Stores user information, including their email, password hash, and role (admin, player, or organizer).
- **Tournaments**: Contains details about each tournament, such as its name, location, start and end dates, and participant limit.
- **Matches**: Records match information, linking tournaments with participating users.

### Tables and Relationships

1. **Users**
   - Fields: `id`, `email`, `password_hash`, `role`, `created_at`, `updated_at`
   - Indexed by: `email`

2. **Tournaments**
   - Fields: `id`, `name`, `location`, `start_date`, `end_date`, `participant_limit`, `created_at`, `updated_at`
   - Indexed by: `name`
   - Relationships: Has many `matches`

3. **Matches**
   - Fields: `id`, `tournament_id`, `player1_id`, `player2_id`, `scheduled_time`, `player1_score`, `player2_score`, `status`, `created_at`, `updated_at`
   - Indexed by: `tournament_id`, `scheduled_time`
   - Relationships: Belongs to `tournaments`, `users` as `player1`, and `users` as `player2`

## Setup Instructions

1. **Database Creation**
   - Ensure PostgreSQL is installed and running.
   - Create a new database: `CREATE DATABASE badminton_db;`

2. **Schema Initialization**
   - Run the schema script: `psql -U user -d badminton_db -f database/schema.sql`

3. **Migrations**
   - Configure Alembic: Update `sqlalchemy.url` in `alembic.ini` with your database credentials.
   - Run migrations: `alembic upgrade head`

4. **Seed Data**
   - Run seed data scripts:
     - SQL: `psql -U user -d badminton_db -f database/seeds/seed_data.sql`
     - Python: `python database/seeds/seed_data.py`

5. **Extensions and Indexes**
   - Ensure the `pgcrypto` extension is enabled for UUID generation.
   - Review and optimize indexes based on query patterns.

## Maintenance and Scalability

- Use `Redis` for caching frequently accessed data, with a 5-minute TTL.
- Leverage horizontal scaling to accommodate increasing load.
- Manage background tasks using `Celery` for operations like sending notifications or processing large datasets.