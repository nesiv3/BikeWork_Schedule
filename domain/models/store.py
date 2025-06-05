from pydantic import BaseModel, EmailStr


class Store(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str
    class Config:
        arbitrary_types_allowed = True