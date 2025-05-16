from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel
from typing import Any, Optional

from utils.config import to_colombia_time
from utils.pyobjectid import PyObjectId






class ScheduleResponse(BaseModel):
    id: Optional[PyObjectId] = None
    date: str  # Ya transformado con strftime
    period: Optional[str] = None
    maintenance_type: int
    status: str
    observation: str
    cost: float
    estimated_time_minutes: int
    user: Any
    store: Any
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_schedule(cls, schedule):
        return cls(
            id=schedule.id,
            date=schedule.date.strftime("%d-%m-%Y"),
            period=str(schedule.period) if schedule.period else None,
            maintenance_type=schedule.maintenance_type,
            status=schedule.status,
            observation=schedule.observation,
            cost=schedule.cost,
            estimated_time_minutes=schedule.estimated_time_minutes,
            user=schedule.user,
            store=schedule.store,
            created_at=to_colombia_time(schedule.created_at),
            updated_at=to_colombia_time(schedule.updated_at),
        )
