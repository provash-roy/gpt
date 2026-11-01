# GPT

This project contains a FastAPI backend and a Next.js frontend.

## Project structure

- `src/gpt/` - FastAPI backend
- `frontend/` - Next.js app (App Router, TypeScript, Tailwind CSS)

## Run the backend

From the project root:

```powershell
uv sync
uv run uvicorn gpt.app:app --reload
```

The backend runs at `http://127.0.0.1:8000`. Its current endpoint is `GET /hello`.

## Run the frontend

In a separate terminal:

```powershell
cd frontend
npm install
npm run dev
```

The frontend runs at `http://localhost:3000`. Edit `frontend/src/app/page.tsx` to
build the home page.