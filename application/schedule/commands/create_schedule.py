from datetime import datetime
from zoneinfo import ZoneInfo
from domain.models.schedule import Schedule
from infraestructure.unit_of_work import UnitOfWork
from utils.email.email_schema import EmailSchema
from utils.email.email import send_email  # llamada directa

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

        fecha = command.schedule.date.strftime("%d-%m-%Y")
        await self._send_user_email(command, fecha)
        await self._send_store_email(command, fecha)

    async def _send_user_email(self, command: CreateScheduleCommand, fecha: str):
        email = EmailSchema(
            sender_name="BikeWork",
            sender_email="nesiv3@gmail.com",
            recipient_name=command.schedule.user.full_name,
            recipient_email=command.schedule.user.email,
            subject="Tu agenda ha sido creada",
            html_content=f"""
                <p>Hola {command.schedule.user.full_name},<br>
                Tu mantenimiento ha sido registrado exitosamente.</p>
                <p>Recuerda que <strong>{command.schedule.store.name}</strong> es el lugar donde debes llevar tu bicicleta 
                para el mantenimiento. Te estará esperando el día <strong>{fecha}</strong>.</p>
                <p>Saludos,<br>BikeWork</p>
            """
        )
        await send_email(email)

    async def _send_store_email(self, command: CreateScheduleCommand, fecha: str):
        email = EmailSchema(
            sender_name="BikeWork",
            sender_email="nesiv3@gmail.com",
            recipient_name=command.schedule.store.name,
            recipient_email=command.schedule.store.email,
            subject="Han registrado un agendamiento",
            html_content=f"""
                <p>Hola {command.schedule.store.name},<br>
                Se ha registrado un mantenimiento para tu tienda.</p>
                <p><strong>{command.schedule.user.full_name}</strong> es la persona que llevará la bicicleta. Espérala el día <strong>{fecha}</strong>.</p>
                <p>Saludos,<br>BikeWork</p>
            """
        )
        await send_email(email)
