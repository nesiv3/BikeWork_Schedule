from zoneinfo import ZoneInfo
from domain.models.store import Store
from domain.models.user import User
from pydantic import BaseModel, Field
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
    created_at: datetime
    updated_at: datetime

   
   
   



    class Config:
        arbitrary_types_allowed = True,
        from_attributes = True