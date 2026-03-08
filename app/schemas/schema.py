from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TripCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = Field(default=None, max_length=4000)


class TripResponse(BaseModel):
    id: str
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None
    created_at: datetime

