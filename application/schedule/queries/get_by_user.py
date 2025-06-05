# application/queries/get_by_store.py
from datetime import datetime

from application.schedule.dbo import ScheduleResponse

class GetScheduleByUserQuery:
    def __init__(self, store_id: int, start: datetime, end: datetime):
        self.store_id = store_id
        self.start = start
        self.end = end

class GetByUserHandler:
    def __init__(self, uow):
        self.uow = uow

    async def handle(self, query: GetScheduleByUserQuery):
        schedules = await self.uow.schedule_repository.get_by_user(query.store_id, query.start, query.end)
        return [ScheduleResponse.from_schedule(s) for s in schedules]
