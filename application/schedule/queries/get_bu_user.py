# application/queries/get_by_store.py
from datetime import datetime

class GetScheduleByUserQuery:
    def __init__(self, store_id: int, start: datetime, end: datetime):
        self.store_id = store_id
        self.start = start
        self.end = end

class GetByUserHandler:
    def __init__(self, uow):
        self.uow = uow

    async def handle(self, query: GetScheduleByUserQuery):
        return await self.uow.schedule_repository.get_by_user(query.store_id, query.start, query.end)
