# trip-planner-service

## Run locally

Create a virtualenv, install deps, and start the server.

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env
uvicorn app.main:app --reload
```

## API

- `GET /api/health`
- `POST /api/trips`
- `GET /api/trips`
- `GET /api/trips/{trip_id}`