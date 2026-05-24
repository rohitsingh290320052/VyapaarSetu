Deployment guide — Render & Railway
=================================

This file explains how to deploy the app to Render or Railway and how to fix the common git/network push problem you saw.

Prereqs
- Push the repository to GitHub (or a Git provider) and ensure CI access.
- Ensure `backend/.env` is populated or set equivalent environment variables on the platform.

Common Git push failure (HTTP 408 / remote disconnect)
- If `git push` failed with "RPC failed" or HTTP 408, try:

  1. Increase Git HTTP buffer (temporary):
  ```powershell
  git config --global http.postBuffer 524288000
  git push origin main
  ```

  2. If repository is large, try pushing with SSH instead of HTTPS:
  - Add your SSH key to GitHub and change remote URL:
  ```powershell
  git remote set-url origin git@github.com:<owner>/<repo>.git
  git push origin main
  ```

  3. If push still fails, push smaller commits or check network/ISP, or use a machine with more reliable connectivity.

Environment variables (required)
- `DATABASE_URL` (postgres connection string — provided by the host service)
- `JWT_SECRET_KEY` (secure random string)
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` (e.g. 30)
- `JWT_REFRESH_TOKEN_EXPIRE_DAYS` (e.g. 7)
- `BACKEND_CORS_ORIGINS` (comma-separated origins for frontend, e.g. https://your-frontend.example.com)

Notes: the repository contains two Dockerfiles:
- `backend/Dockerfile` — builds the FastAPI app
- `frontend/Dockerfile` — builds the Next.js app

A. Deploy to Render (recommended simple path)
1. Create a new Web Service -> Connect your GitHub repo
2. For the backend service:
   - Environment: Docker
   - Root: set to the repository root, then set the "Dockerfile path" to `/backend/Dockerfile` (or use the `backend` folder)
   - Start Command: leave default (Render will use Dockerfile CMD), or set explicitly:
     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
     ```
   - Add environment variables in the Render dashboard (see list above)
   - (Optional) Add a "Post Deploy" or "Start command" to run migrations:
     - Use a Render "Startup Command" or add a one-off service that runs:
       ```bash
       alembic upgrade head
       ```
3. For the frontend service:
   - Create a new Web Service
   - Dockerfile path: `/frontend/Dockerfile`
   - Set `NODE_ENV=production` in env vars
   - The container will serve on port 3000
4. Verify services are healthy, check logs in Render dashboard

B. Deploy to Railway
1. Create a new project and connect your GitHub repo
2. Add a Postgres plugin (Railway will provide `DATABASE_URL`)
3. Create two services (or one service per component):
   - Backend service: choose Dockerfile and point to `/backend` folder (Railway supports subdirectory Dockerfile)
   - Frontend service: choose Dockerfile and point to `/frontend` folder or deploy the frontend with Vercel
4. Add env vars in Railway project settings:
   - Set `JWT_SECRET_KEY`, `BACKEND_CORS_ORIGINS`, etc.
5. Add a "deploy hook" or run migrations after build:
   - Railway provides a console — run `alembic upgrade head` once, or add a release command if using their "start" configuration.

Running Alembic migrations on these platforms
- Best practice: run `alembic upgrade head` after the DB is provisioned and `DATABASE_URL` is set.
- Render: use a startup hook or run a one-off instance that executes `alembic upgrade head`.
- Railway: run the Railway console command or an one-off task with `docker compose run backend alembic upgrade head` replaced by the Dockerfile equivalent: `alembic upgrade head` in the built container.

Health checks and verification
- Backend: `https://<backend-service>/api/v1/group-orders` should return empty list or unauthorized depending on setup.
- Frontend: open the frontend URL to confirm static pages load.

If you want, I can:
- Generate `render.yaml` for Render if you prefer infrastructure-as-code, or
- Create a simple GitHub Actions workflow to build and push Docker images to Docker Hub / GitHub Container Registry and then trigger a deploy.

