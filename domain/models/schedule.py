from domain.models.store import Store
from domain.models.user import User
from pydantic import BaseModel
from datetime import datetime

class Schedule(BaseModel):
    date: datetime
    maintenance_type: int
    status: str
    observation: str
    cost: float
    estimated_time_minutes: int
    user: User
    store: Store
    class Config:
        arbitrary_types_allowed = True,
        from_attributes = True