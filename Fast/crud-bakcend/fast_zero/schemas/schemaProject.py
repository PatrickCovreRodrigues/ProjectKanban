from pydantic import BaseModel


class ProjectCreate(BaseModel):
    id: int
    name: str
    description_activity: str
    customer_project: int
