# application/queries/get_by_store.py
from datetime import datetime

class GetScheduleByStoreQuery:
    def __init__(self, store_id: int, start: datetime, end: datetime):
        self.store_id = store_id
        self.start = start
        self.end = end

class GetByStoreHandler:
    def __init__(self, uow):
        self.uow = uow

    async def handle(self, query: GetScheduleByStoreQuery):
        return await self.uow.schedule_repository.get_by_store(query.store_id, query.start, query.end)
