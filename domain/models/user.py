from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    phone_number: str
    class Config:
        arbitrary_types_allowed = True