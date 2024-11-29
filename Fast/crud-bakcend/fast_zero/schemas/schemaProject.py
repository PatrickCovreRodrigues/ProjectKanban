from pydantic import BaseModel
from typing import List


class ProjectCreate(BaseModel):
    id: int
    name: str
    description_project: str
    customer_project: int


class ListProject(BaseModel):
    project_list: List[ProjectCreate]