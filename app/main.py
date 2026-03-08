from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.endpoints.endpoint import router as trips_router
from app.core.database import close_mongo_connection, connect_to_mongo


@asynccontextmanager
async def lifespan(_: FastAPI):
    connect_to_mongo()
    try:
        yield
    finally:
        close_mongo_connection()


def create_app() -> FastAPI:
    app = FastAPI(title="Trip Planner Service", version="0.1.0", lifespan=lifespan)

    app.include_router(trips_router, prefix="/api")

    return app


app = create_app()

