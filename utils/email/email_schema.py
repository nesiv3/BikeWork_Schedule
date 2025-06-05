from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    sender_name: str
    sender_email: EmailStr
    recipient_name: str
    recipient_email: EmailStr
    subject: str
    html_content: str