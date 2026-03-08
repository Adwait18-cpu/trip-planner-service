from __future__ import annotations

from typing import Any, List, Optional

from bson import ObjectId

from app.core.database import get_db


class TripRepository:
    def __init__(self) -> None:
        self.db = get_db()
        self.collection = self.db["trips"]

    async def insert_trip(self, trip: dict[str, Any]) -> dict[str, Any]:
        result = await self.collection.insert_one(trip)
        created = await self.collection.find_one({"_id": result.inserted_id})
        assert created is not None
        return created

    async def list_trips(self, limit: int = 50) -> List[dict[str, Any]]:
        cursor = self.collection.find({}).sort("created_at", -1).limit(max(1, min(limit, 500)))
        return [doc async for doc in cursor]

    async def get_trip_by_id(self, trip_id: str) -> Optional[dict[str, Any]]:
        if not ObjectId.is_valid(trip_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(trip_id)})

