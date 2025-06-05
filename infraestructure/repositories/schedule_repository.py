from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.repositories.schedule_repository import ScheduleRepository
from domain.models.schedule import Schedule
from typing import List
from datetime import datetime
from bson import ObjectId

class ScheduleRepositoryMongo(ScheduleRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["schedule"]

    async def add(self, schedule: Schedule):
        await self.collection.insert_one(schedule.dict())

    async def get_by_store(self, store_id: int, start: datetime, end: datetime) -> List[Schedule]:
        cursor = self.collection.find({
            "store.id": store_id,
            "date": {"$gte": start, "$lte": end}
        })
        return [Schedule(**doc) async for doc in cursor]

    async def get_by_user(self, user_id: str, start: datetime, end: datetime) -> List[Schedule]:
        cursor = self.collection.find({
            "user.id": user_id,
            "date": {"$gte": start, "$lte": end}
        })
        return [Schedule(**doc) async for doc in cursor]
    
    async def update(self, schedule_id: str, update_data: Schedule):
        await self.collection.update_one(
            {"_id": ObjectId(schedule_id)},
            {"$set": update_data.dict()}
        )
