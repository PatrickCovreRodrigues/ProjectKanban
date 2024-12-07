from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session
from fast_zero.models.model import Activity, User
from fast_zero.schemas.schemaActivity import ActivityCreate

router = APIRouter(
    prefix='/activity',
    tags=['activity'],
)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ActivityCreate)
def activity_created(activity: ActivityCreate, session: Session = Depends(get_session)):
    customer_user = session.scalar(
        select(User).where(User.id == activity.customer_id)
    )
    if not customer_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Cliente não existe'
        )
    activity_creat = session.scalar(
        select(Activity).where(Activity.id == activity.id)
    )
    if activity_creat:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Atividade já existe'
        )
    new_activity = Activity(
        name=activity.name,
        description_activity=activity.description_activity,
        customer_id=activity.customer_id
    )
    session.add(new_activity)
    session.commit()
    session.refresh(new_activity)

    return new_activity


@router.get('/{activity_id}', response_model=ActivityCreate)
def read_activity(
    activity_id: int,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada!'
        )
    return db_activity


@router.put('/{activity_id}', response_model=ActivityCreate,)
def update_activity(
    activity_id: int,
    activity: ActivityCreate,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada'
        )
    if not activity.customer_id:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado'
        )
    db_activity.name = activity.name
    db_activity.description_activity = activity.description_activity
    db_activity.customer_id = activity.customer_id
    session.commit()
    session.refresh(db_activity)

    return db_activity


@router.delete('/{activity_id}', response_model=dict)
def delete_activity(
    activity_id: int,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada'
        )
    session.delete(db_activity)
    session.commit()
    return {'message': 'Atividade Deletada'}
