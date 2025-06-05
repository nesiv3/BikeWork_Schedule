
from domain.repositories.schedule_repository import ScheduleRepository
from infraestructure.repositories.schedule_repository import ScheduleRepositoryMongo

class UnitOfWork:
    def __init__(self, schedule_repository: ScheduleRepository):
        self.schedule_repository = schedule_repository

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass
