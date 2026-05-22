# RetailLink

RetailLink is a venture-grade Direct-to-Retailer commerce platform enabling local retailers to pool demand, unlock MOQ pricing, and order directly from manufacturers.

## Architecture

- Frontend: Next.js 15 (App Router), TypeScript, TailwindCSS, Shadcn UI, TanStack Query
- Backend: FastAPI, PostgreSQL, SQLAlchemy, JWT auth, WebSocket event layer
- Infrastructure: Docker, Docker Compose

## Project structure

- `backend/` - FastAPI backend with modular domain packages
- `frontend/` - Next.js application with reusable UI system
- `docker-compose.yml` - local development stack for backend, frontend, postgres

## Getting started

1. Copy `.env.example` to `.env` and update values
2. Start containers:
   ```bash
   docker compose up --build
   ```
3. Backend: `http://localhost:8000`
4. Frontend: `http://localhost:3000`

## Next steps

- implement auth, onboarding, group-buy engine, payments, analytics, logistics.
- add seed scripts and migrations.
