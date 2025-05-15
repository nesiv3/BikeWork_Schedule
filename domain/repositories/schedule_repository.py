from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from domain.models.schedule import Schedule

class ScheduleRepository(ABC):

    @abstractmethod
    async def add(self, schedule: Schedule):
        pass

    @abstractmethod
    async def get_by_store(self, store_id: int, start: datetime, end: datetime) -> List[Schedule]:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int, start: datetime, end: datetime) -> List[Schedule]:
        pass
