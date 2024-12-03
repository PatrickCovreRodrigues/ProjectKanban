from pydantic import BaseModel


class ActivityCreate(BaseModel):
    id: int
    name: str
    description_activity: str
    customer_id: int
