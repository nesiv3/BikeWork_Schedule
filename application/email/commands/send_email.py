from utils.email.email_schema import EmailSchema
from utils.email.email import send_email  

class SendEmailCommand:
    def __init__(self, email: EmailSchema):
        self.email = email

class SendEmailHandler:
    async def handle(self, command: SendEmailCommand):
        await send_email(command.email)