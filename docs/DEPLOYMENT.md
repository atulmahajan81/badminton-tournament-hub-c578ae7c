# Deployment Guide

This document outlines the steps for deploying the Badminton Tournament Hub using Docker.

## Docker Deployment

1. **Build and Start Services**
   ```bash
   docker-compose up --build
   ```

2. **Access the Application**
   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:8000`

## Environment Variables

| Variable Name     | Description                               |
| ----------------- | ----------------------------------------- |
| `DATABASE_URL`    | Connection string for the PostgreSQL DB   |
| `REDIS_URL`       | Connection string for the Redis cache     |
| `SECRET_KEY`      | Secret key for JWT encoding               |

## Scaling Guide

- Use `docker-compose scale <service>=<number>` to scale services horizontally.

## Monitoring

- Set up logging and monitoring using tools like Prometheus and Grafana for real-time insights into application performance.