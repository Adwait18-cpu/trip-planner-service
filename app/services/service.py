from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, List

from app.repositories.repository import TripRepository


class NotFoundError(Exception):
    pass


class TripService:
    def __init__(self) -> None:
        self.repo = TripRepository()

    async def create_trip(self, data: dict[str, Any]) -> dict[str, Any]:
        data = dict(data)
        data["created_at"] = datetime.now(timezone.utc)
        return await self.repo.insert_trip(data)

    async def list_trips(self, limit: int = 50) -> List[dict[str, Any]]:
        return await self.repo.list_trips(limit=limit)

    async def get_trip(self, trip_id: str) -> dict[str, Any]:
        trip = await self.repo.get_trip_by_id(trip_id)
        if trip is None:
            raise NotFoundError(f"Trip not found: {trip_id}")
        return trip

