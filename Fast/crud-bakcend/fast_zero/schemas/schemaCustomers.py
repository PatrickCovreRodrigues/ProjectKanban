from pydantic import BaseModel, EmailStr
from typing import List



class CustomerCreate(BaseModel):
    id: int
    name: str
    description: str
    email: EmailStr


class CustomerList(BaseModel):
    customers: List[CustomerCreate]