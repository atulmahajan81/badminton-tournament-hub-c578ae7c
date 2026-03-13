# API Reference

This document provides a comprehensive reference for the API endpoints available in the Badminton Tournament Hub.

## Authentication

### `POST /api/v1/auth/register`

Registers a new user.

- **Request Body**
  ```json
  {
    "email": "string",
    "password": "string",
    "role": "string"
  }
  ```

- **Response**
  ```json
  {
    "id": "UUID",
    "email": "string"
  }
  ```

### `POST /api/v1/auth/login`

Authenticates a user and returns an access token.

- **Request Body**
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```

- **Response**
  ```json
  {
    "access_token": "string",
    "refresh_token": "string"
  }
  ```

## Tournaments

### `POST /api/v1/tournaments`

Creates a new tournament.

- **Request Body**
  ```json
  {
    "name": "string",
    "location": "string",
    "start_date": "date",
    "end_date": "date",
    "participant_limit": "integer"
  }
  ```

- **Response**
  ```json
  {
    "id": "UUID",
    "name": "string"
  }
  ```

### `GET /api/v1/tournaments`

Retrieves a list of all tournaments.

- **Response**
  ```json
  [
    {
      "id": "UUID",
      "name": "string",
      "location": "string"
    }
  ]
  ```

Refer to the full API documentation for a complete list of available endpoints.