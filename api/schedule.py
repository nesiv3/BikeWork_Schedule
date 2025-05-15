# api/routes/maintenance.py
from zoneinfo import ZoneInfo
from fastapi import APIRouter, Depends, Query
from datetime import datetime
from domain.models.schedule import Schedule
from utils.container import Container
from application.schedule.commands.create_schedule import CreateScheduleCommand
from application.schedule.queries.get_by_store import GetScheduleByStoreQuery
from application.schedule.queries.get_by_user import GetScheduleByUserQuery

router = APIRouter()

@router.post("/")
async def create_maintenance(schedule: Schedule):
    dispatcher = Container.instance().dispatcher
    now = datetime.now(ZoneInfo("America/Bogota")) 
    schedule.created_at = now
    schedule.updated_at = now
 
    await dispatcher.dispatch(CreateScheduleCommand(schedule))
    return {"status": "created"}

@router.get("/store/{store_id}")
async def get_by_store(store_id: int, start: datetime = Query(...), end: datetime = Query(...)):
    dispatcher = Container.instance().dispatcher
    result = await dispatcher.dispatch(GetScheduleByStoreQuery(store_id, start, end))
    return result

@router.get("/user/{user_id}")
async def get_by_user(user_id: str, start: datetime = Query(...), end: datetime = Query(...)):
    dispatcher = Container.instance().dispatcher
    result = await dispatcher.dispatch(GetScheduleByUserQuery(user_id, start, end))
    return result



@router.get("/health")
async def healt():
   now = datetime.now(ZoneInfo("America/Bogota")) 
   return now
