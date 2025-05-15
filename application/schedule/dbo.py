from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel
from typing import Any

from utils.config import to_colombia_time






class ScheduleResponse(BaseModel):
    date: str  # Ya transformado con strftime
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
            date=schedule.date.strftime("%d-%m-%Y"),
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
