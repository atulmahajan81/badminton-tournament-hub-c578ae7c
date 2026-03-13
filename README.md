# Badminton Tournament Hub

![Test Coverage](https://img.shields.io/badge/Coverage-95%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

**Seamless tournament management for players, organizers, and umpires**

Badminton Tournament Hub is designed to simplify the management of badminton tournaments, providing tools for tournament creation, player registration, match scheduling, and more.

## Features

- ✓ Tournament Creation
- ✓ Player Registration
- ✓ Match Scheduling
- ✓ Score Reporting
- ✓ Notifications
- ✓ Tournament Dashboard
- ✓ User Authentication
- ✓ Role-Based Access Control

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/badminton-tournament-hub.git

# Navigate into the directory
cd badminton-tournament-hub

# Start the application using Docker Compose
docker-compose up --build
```

## Prerequisites

| Tool          | Version   |
| ------------- | --------- |
| Docker        | 20.10+    |
| docker-compose| 1.29+     |
| Python        | 3.9+      |
| Node.js       | 16+       |

## Complete Docker Compose Setup

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/tournament
    ports:
      - "8000:8000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tournament

  redis:
    image: redis:7

  nginx:
    image: nginx
    ports:
      - "80:80"
    depends_on:
      - frontend
```

## API Usage Examples

### Register a new user

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepassword", "role": "player"}'
```

### Get all tournaments

```bash
curl -X GET http://localhost:8000/api/v1/tournaments \
  -H "Authorization: Bearer <your-access-token>"
```

## Environment Variables

| Name                 | Required | Default                     | Description                   |
| -------------------- | -------- | --------------------------- | ----------------------------- |
| `DATABASE_URL`       | Yes      | `postgresql://user:pass@localhost:5432/tournament` | Connection string for the PostgreSQL database |
| `REDIS_URL`          | No       | `redis://localhost:6379`    | Redis server URL             |
| `SECRET_KEY`         | Yes      |                             | Key used for JWT encoding    |

## Architecture Diagram

```mermaid
graph TD;
  A[User] -->|Register/Login| B[Auth API];
  B --> C{Database};
  B --> D[Redis Cache];
  C --> E[Tournaments API];
  E --> F[Tournament Management];
  F -->|Notifications| G[Users];
```

## Tech Stack

| Component     | Technology           |
| ------------- | -------------------- |
| Backend       | Python, FastAPI      |
| Frontend      | Next.js, TypeScript  |
| Database      | PostgreSQL, Redis    |
| Infrastructure| Docker, Nginx        |

For more detailed documentation, please refer to the [docs folder](./docs/).

## License

This project is licensed under the MIT License.