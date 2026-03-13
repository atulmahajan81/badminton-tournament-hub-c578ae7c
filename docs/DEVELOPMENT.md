# Development Guide

This guide provides instructions for setting up the development environment for the Badminton Tournament Hub project.

## Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/badminton-tournament-hub.git
   cd badminton-tournament-hub
   ```

2. **Set Up Python Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```

3. **Install Frontend Dependencies**
   ```bash
   cd frontend
   npm install
   ```

4. **Run the Development Server**
   - Backend: `uvicorn backend.main:app --reload`
   - Frontend: `npm run dev`

## Running Tests

- **Backend Tests**
  ```bash
  pytest
  ```

- **Frontend Tests**
  ```bash
  npm run test
  ```

## Code Structure

- **Backend**: Located in the `backend/` directory with separate modules for auth, tournaments, and notifications.
- **Frontend**: Located in the `frontend/` directory with components, pages, and styles split by function and view.

## Contributing Guide

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.