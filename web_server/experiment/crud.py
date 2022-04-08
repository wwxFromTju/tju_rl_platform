import os
import uuid

from sqlalchemy.orm import Session

import schemas
import dataset_models
from project.crud import get_project_by_id


def create_user_project_experiment(db: Session, experiment: schemas.ExperimentCreate, project_id: int, user_id: int):
    experiment_id = len(get_experiments(db, user_id=user_id, project_id=project_id))

    experiment.parameter = str(experiment.parameter)

    project = get_project_by_id(db, user_id=user_id, project_id=project_id)
    log_path = os.path.join(project.log_path, str(uuid.uuid1()))
    os.mkdir(log_path)
    
    db_experiment = dataset_models.Experiment(**experiment.dict(), project_id=project_id, owner_id=user_id, log_path=log_path, id=experiment_id+1)
    db.add(db_experiment)
    db.commit()
    db.refresh(db_experiment)
    return db_experiment

def get_experiments(db: Session, user_id: int, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(dataset_models.Experiment).filter(dataset_models.Experiment.owner_id == user_id,
                                                    dataset_models.Experiment.project_id == project_id).offset(skip).limit(limit).all()


def get_experiments_by_id(db: Session, user_id: int, project_id: int, experiment_id: int):
    return db.query(dataset_models.Experiment).filter(dataset_models.Experiment.owner_id == user_id,
                                                   dataset_models.Experiment.project_id == project_id,
                                                   dataset_models.Experiment.id == experiment_id).first()


def stop_experiments_by_id(db: Session, user_id: int, project_id: int, experiment_id: int):
    experiment = get_experiments_by_id(db, user_id=user_id, project_id=project_id, experiment_id=experiment_id)
    experiment.is_active = False
    db.commit()
    db.refresh(experiment)
    return experiment
