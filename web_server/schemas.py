from typing import Dict, Optional

from pydantic import BaseModel


class ExperimentBase(BaseModel):
    title: str
    description: Optional[str] = None
    parameter: Dict
    

class ExperimentCreate(ExperimentBase):
    pass


class Experiment(ExperimentBase):
    id: int
    project_id: int
    owner_id: int
    log_path: str
    parameter: str
    is_active: bool
    metric: Optional[Dict] = None

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    project_type: str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    owner_id: int
    log_path: str
    experiments: Optional[list] = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    projects: Optional[list] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None