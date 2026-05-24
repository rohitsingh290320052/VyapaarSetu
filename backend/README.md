# Backend Setup

This backend is a FastAPI app using SQLAlchemy and PostgreSQL.

## Recommended local workflows

### Option A: Docker-based development (best for Windows)

This avoids `asyncpg` build issues on Windows.

```powershell
cd D:\Fix my Itch
docker compose up --build
```

This starts:
- `postgres` on port `5432`
- backend on port `8000`
- frontend on port `3000`

The backend service uses `backend/.env.example` for environment variables.

### Option B: Local Python dev on Windows

1. Create a virtual environment:

```powershell
cd D:\Fix my Itch\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

> If `asyncpg` fails to build, install Visual C++ Build Tools from:
> `https://visualstudio.microsoft.com/visual-cpp-build-tools/`

3. Set your environment variable in PowerShell:

```powershell
$env:DATABASE_URL = 'postgresql+asyncpg://retailink:retailinkpass@localhost:5432/retailink'
```

4. Run Alembic migrations:

```powershell
alembic upgrade head
```

5. Start the app:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Migrations

Alembic is configured in `backend/alembic.ini` and `backend/alembic/env.py`.

The initial schema migration is available at `backend/alembic/versions/0001_initial.py`.

### To create future migrations

```powershell
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Environment variables

The backend uses `backend/.env.example` and expects:

- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`
- `JWT_REFRESH_TOKEN_EXPIRE_DAYS`

For development, copy `.env.example` to `.env` if you want a local file.

## Notes

- The app no longer calls `Base.metadata.create_all(...)` on startup.
- Database schema should be managed through Alembic migrations.
- If you use Docker, the backend will still read the same `.env.example` values unless you override them.
