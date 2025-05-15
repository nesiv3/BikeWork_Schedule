from motor.motor_asyncio import AsyncIOMotorClient
from infraestructure.repositories.schedule_repository import ScheduleRepositoryMongo
from infraestructure.unit_of_work import UnitOfWork
from application.schedule.commands.create_schedule import CreateScheduleCommand, CreateScheduleHandler
from application.schedule.queries.get_by_store import GetByStoreHandler, GetScheduleByStoreQuery
from application.schedule.queries.get_bu_user import GetByUserHandler, GetScheduleByUserQuery
from application.mediators.dispatcher import Dispatcher

class Container:
    _instance = None

    @staticmethod
    def instance():
        if not Container._instance:
            Container._instance = Container()
        return Container._instance

    def __init__(self):
        client = AsyncIOMotorClient("mongodb+srv://nesiv3:bUdhLOKPpudxbXWj@bikework.omnndyc.mongodb.net/?retryWrites=true&w=majority&appName=bikework")
        db = client["schedule"]

        repo = ScheduleRepositoryMongo(db)
        uow = UnitOfWork(repo)

        self.dispatcher = Dispatcher()
        self.dispatcher.register(CreateScheduleCommand, CreateScheduleHandler(uow))
        self.dispatcher.register(GetScheduleByStoreQuery, GetByStoreHandler(uow))
        self.dispatcher.register(GetScheduleByUserQuery, GetByUserHandler(uow))
