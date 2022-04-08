import os
import uuid

from sqlalchemy.orm import Session

import schemas
import dataset_models
from config import LOG_DIR

def create_user_project(db: Session, project: schemas.ProjectCreate, user_id: int):
    project_id = len(get_projects(db, user_id=user_id))

    log_path = os.path.join(LOG_DIR, str(uuid.uuid1()))
    os.mkdir(log_path)
    db_project = dataset_models.Project(**project.dict(), owner_id=user_id, log_path=log_path, id=project_id+1)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(dataset_models.Project).filter(dataset_models.Project.owner_id == user_id).offset(skip).limit(limit).all()


def get_project_by_id(db: Session, user_id: int, project_id: int):
    return db.query(dataset_models.Project).filter(dataset_models.Project.owner_id == user_id,dataset_models.Project.id == project_id).first()

