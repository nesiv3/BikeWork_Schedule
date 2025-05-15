
from domain.models.schedule import Schedule
from infraestructure.unit_of_work import UnitOfWork

class CreateScheduleCommand:
    def __init__(self, schedule: Schedule):
        self.schedule = schedule

class CreateScheduleHandler:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: CreateScheduleCommand):
        async with self.uow:
            await self.uow.schedule_repository.add(command.schedule)
