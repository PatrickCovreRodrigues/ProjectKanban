from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session
from fast_zero.models.model import Project, User
from fast_zero.schemas.schemaProject import ProjectCreate,  ListProject
from fast_zero.schemas.schemaMessage import Message

router = APIRouter(
    prefix='/project',
    tags=['project']
)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ProjectCreate)
def project_created(project: ProjectCreate, session: Session = Depends(get_session)):
    customer_id = session.scalar(
        select(User).where(User.id == project.customer_project)
    )
    if not customer_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Cliente não existe!'
        )
    project_creat = session.scalar(
        select(Project).where(Project.id == project.id)
    )
    if project_creat:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Projeto já existe'
        )
    new_project = Project(
        name=project.name,
        description_project=project.description_project,
        customer_id=project.customer_project
    )
    session.add(new_project)
    session.commit()
    session.refresh(new_project)

    return new_project


@router.get('/', response_model=ListProject)
def read_project(session: Session=Depends(get_session)):
    project_list = session.query(Project).all()
    return{'project_list': project_list}


@router.get('/{project_id}', response_model=ProjectCreate)
def read_project_id(project_id: int, session: Session = Depends(get_session)):
    db_project = session.scalar(select(Project).where(Project.id == project_id))
    if not db_project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )


@router.put('/{project_id}', response_model=ProjectCreate)
def update_project_id(
    project_id: int,
    project: ProjectCreate,
    session: Session = Depends(get_session)
):
    db_project = session.scalar(select(Project).where(Project.id == project_id))
    if not db_project():
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    db_customer = session.scalar(select(User).where(User.id == project.customer_project))
    if not db_customer:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não existe!'
        )
    db_project.name=project.name
    db_project.description_activity=project.description_project
    db_project.customer_project=project.customer_project

    return db_project


@router.delete('/{project_id}', response_model=Message)
def delete_project(project_id: int, session: Session = Depends(get_session)):
    db_project = session.scalar(select(Project).where(Project.id == project_id))
    if not db_project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    session.delete(db_project)
    session.commit()
    return {'message': 'Projeto excluido'}