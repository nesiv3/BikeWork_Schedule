from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from domain.models.user import User
from domain.models.store import Store

class ScheduleDTO(BaseModel):
    date: datetime
    period: Optional[str]
    maintenance_type: int
    status: str
    observation: str
    cost: float
    estimated_time_minutes: int
    user: User
    store: Store
    created_at: datetime
    updated_at: datetime
