from datetime import datetime
from zoneinfo import ZoneInfo
from application.email.commands import send_email
from application.schedule.schedule_update_dto import ScheduleDTO
from domain.models.schedule import Schedule
from infraestructure.unit_of_work import UnitOfWork
from utils.email.email_schema import EmailSchema
from utils.email.email import send_email  # llamada directa

class UpdateScheduleCommand:
    def __init__(self,schedule_id,schedule: ScheduleDTO):
         self.schedule_id = schedule_id
         self.schedule = schedule
        #self.data = schedule  # Solo campos principales a actualizar

class UpdateScheduleHandler:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def handle(self, command: UpdateScheduleCommand):
            command.schedule.updated_at = datetime.now(ZoneInfo("America/Bogota"))
            async with self.uow:
                await self.uow.schedule_repository.update(command.schedule_id,command.schedule)
            
            fecha = command.schedule.date.strftime("%d-%m-%Y")
            await self._send_user_email(command, fecha)
            await self._send_store_email(command, fecha)


    

    async def _send_user_email(self, command: UpdateScheduleCommand, fecha: str):
        email = EmailSchema(
            sender_name="BikeWork",
            sender_email="nesiv3@gmail.com",
            recipient_name=command.schedule.user.full_name,
            recipient_email=command.schedule.user.email,
            subject="Tu agenda ha sido modificado",
            html_content=f"""
                <p>Hola {command.schedule.user.full_name},<br>
                Tu mantenimiento ha sido modificado exitosamente.</p>
                <p>Recuerda que <strong>{command.schedule.store.name}</strong> es el lugar donde debes llevar tu bicicleta 
                para el mantenimiento. Te estará esperando el día <strong>{fecha}</strong>.</p>
                <p>Saludos,<br>BikeWork</p>
            """
        )
        await send_email(email)

    async def _send_store_email(self, command: UpdateScheduleCommand, fecha: str):
        email = EmailSchema(
            sender_name="BikeWork",
            sender_email="nesiv3@gmail.com",
            recipient_name=command.schedule.store.name,
            recipient_email=command.schedule.store.email,
            subject="Han modificado un agendamiento",
            html_content=f"""
                <p>Hola {command.schedule.store.name},<br>
                Se ha modificado un mantenimiento para tu tienda.</p>
                <p><strong>{command.schedule.user.full_name}</strong> es la persona que llevará la bicicleta. Espérala el día <strong>{fecha}</strong>.</p>
                <p>Saludos,<br>BikeWork</p>
            """
        )
        await send_email(email)