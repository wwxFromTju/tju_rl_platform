from distutils.command.config import config
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

# from ..dependencies import get_token_header
import schemas
from project import crud
import config
from user.user_router import get_current_active_user

# Dependency
def get_db(request: Request):
    return request.state.db

router = APIRouter(
    prefix="/users/{user_id}/projects",
    tags=["projects"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Project)
def create_project_for_user(
    user_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    assert project.project_type in config.project_config, f'{project.project_type} support [x]'
    return crud.create_user_project(db=db, project=project, user_id=user_id)


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(user_id: int, project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db, user_id=user_id, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/", response_model=list[schemas.Project])
def read_projects(user_id: int, db: Session = Depends(get_db)):
    db_projects = crud.get_projects(db, user_id=user_id)
    return db_projects
