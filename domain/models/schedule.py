from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel, Field
from utils.pyobjectid import PyObjectId  # ✅ usa el tipo personalizado
from domain.models.store import Store
from domain.models.user import User

class Schedule(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    date: datetime
    period: Optional[str] = None
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
        arbitrary_types_allowed = True
        from_attributes = True
        populate_by_name = True
