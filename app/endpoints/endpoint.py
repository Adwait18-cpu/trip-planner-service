from typing import Any, List

from fastapi import APIRouter, HTTPException

from app.services.service import NotFoundError, TripService
from app.schemas.schema import TripCreateRequest, TripResponse

router = APIRouter(tags=["trips"])


def _doc_to_trip(doc: dict[str, Any]) -> TripResponse:
    return TripResponse(
        id=str(doc["_id"]),
        name=doc["name"],
        start_date=doc.get("start_date"),
        end_date=doc.get("end_date"),
        notes=doc.get("notes"),
        created_at=doc["created_at"],
    )


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/trips", response_model=TripResponse)
async def create_trip(payload: TripCreateRequest) -> TripResponse:
    service = TripService()
    created = await service.create_trip(payload.model_dump())
    return _doc_to_trip(created)


@router.get("/trips", response_model=List[TripResponse])
async def list_trips(limit: int = 50) -> List[TripResponse]:
    service = TripService()
    docs = await service.list_trips(limit=limit)
    return [_doc_to_trip(d) for d in docs]


@router.get("/trips/{trip_id}", response_model=TripResponse)
async def get_trip(trip_id: str) -> TripResponse:
    service = TripService()
    try:
        doc = await service.get_trip(trip_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return _doc_to_trip(doc)

