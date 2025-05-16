import os
from application.email.commands.send_email import SendEmailCommand, SendEmailHandler
from application.schedule.commands.update_schedule import UpdateScheduleCommand, UpdateScheduleHandler
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from infraestructure.repositories.schedule_repository import ScheduleRepositoryMongo
from infraestructure.unit_of_work import UnitOfWork
from application.schedule.commands.create_schedule import CreateScheduleCommand, CreateScheduleHandler
from application.schedule.queries.get_by_store import GetByStoreHandler, GetScheduleByStoreQuery
from application.schedule.queries.get_by_user import GetByUserHandler, GetScheduleByUserQuery
from application.mediators.dispatcher import Dispatcher



load_dotenv()  
class Container:
    _instance = None

    @staticmethod
    def instance():
        if not Container._instance:
            Container._instance = Container()
        return Container._instance

    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        mongo_db = os.getenv("MONGO_DB")
        client = AsyncIOMotorClient(mongo_uri)
        db = client[mongo_db]
              
        repo = ScheduleRepositoryMongo(db)
        uow = UnitOfWork(repo)

        self.dispatcher = Dispatcher()
        self.dispatcher.register(CreateScheduleCommand, CreateScheduleHandler(uow))
        self.dispatcher.register(GetScheduleByStoreQuery, GetByStoreHandler(uow))
        self.dispatcher.register(GetScheduleByUserQuery, GetByUserHandler(uow))
        self.dispatcher.register(UpdateScheduleCommand, UpdateScheduleHandler(uow))
       
