import importlib
import ast

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

# from ..dependencies import get_token_header
import schemas
from experiment import crud
import config
from experiment.experiment_util import dispatch, kill
from user.user_router import get_current_active_user

# Dependency
def get_db(request: Request):
    return request.state.db

router = APIRouter(
    prefix="/users/{user_id}/projects/{project_id}/experiments",
    tags=["experiments"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Experiment)
def create_experiment_for_project(
    user_id: int, project_id: int, experiment: schemas.ExperimentCreate, db: Session = Depends(get_db)
):
    db_experiment = crud.create_user_project_experiment(db=db, experiment=experiment, user_id=user_id, project_id=project_id)

    project_config = config.project_config[db_experiment.project.project_type]

    train = importlib.import_module(f'project_register.{project_config["entry_path"]}').train

    dispatch(
            f'{db_experiment.project.owner.id}-{db_experiment.project.id}-{db_experiment.id}',
            train,
            project_file_path=project_config['train_file_path'],
            python_path=project_config['python_path'],
            params=ast.literal_eval(db_experiment.parameter),
            logdir=db_experiment.log_path
        )

    return db_experiment


@router.get("/", response_model=list[schemas.Experiment])
def read_experiments(user_id: int, project_id: int, db: Session = Depends(get_db)):
    db_experiments = crud.get_experiments(db, user_id=user_id, project_id=project_id)
    if db_experiments is []:
        return db_experiments
    project_config = config.project_config[db_experiments[0].project.project_type]
    get_metrics = importlib.import_module(f'project_register.{project_config["entry_path"]}').get_metrics
    for idx, db_experiment in enumerate(db_experiments):
        db_experiment.metric = get_metrics(db_experiment.log_path)
    return db_experiments


@router.get("/{experiment_id}", response_model=schemas.Experiment)
def read_experiment(user_id: int, project_id: int, experiment_id: int, db: Session = Depends(get_db)):
    db_experiment = crud.get_experiments_by_id(db, user_id=user_id, project_id=project_id, experiment_id=experiment_id)
    if db_experiment is None:
        raise HTTPException(status_code=404, detail="Experiment not found")

    project_config = config.project_config[db_experiment.project.project_type]
    get_metrics = importlib.import_module(f'project_register.{project_config["entry_path"]}').get_metrics
    db_experiment.metric = get_metrics(db_experiment.log_path)
    return db_experiment


@router.post("/{experiment_id}/stop", response_model=schemas.Experiment)
def stop_experiment(user_id: int, project_id: int, experiment_id: int, db: Session = Depends(get_db)):
    db_experiment = crud.get_experiments_by_id(db, user_id=user_id, project_id=project_id, experiment_id=experiment_id)
    if db_experiment is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_experiment = crud.stop_experiments_by_id(db, user_id=user_id, project_id=project_id, experiment_id=experiment_id)

    project_config = config.project_config[db_experiment.project.project_type]
    get_metrics = importlib.import_module(f'project_register.{project_config["entry_path"]}').get_metrics
    db_experiment.metric = get_metrics(db_experiment.log_path)

    kill(f'{db_experiment.project.owner.id}-{db_experiment.project.id}-{db_experiment.id}')

    return db_experiment