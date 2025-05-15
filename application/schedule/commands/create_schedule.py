
from datetime import datetime
from zoneinfo import ZoneInfo
from domain.models.schedule import Schedule
from infraestructure.unit_of_work import UnitOfWork

class CreateScheduleCommand:
    def __init__(self, schedule: Schedule):
        self.schedule = schedule

class CreateScheduleHandler:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: CreateScheduleCommand):
        now = datetime.now(ZoneInfo("America/Bogota"))       
        command.schedule.created_at = now
        command.schedule.updated_at = now     
        async with self.uow:
            await self.uow.schedule_repository.add(command.schedule)
