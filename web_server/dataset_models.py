from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    project_type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    log_path = Column(String, unique=True)

    owner = relationship("User", back_populates="projects")
    experiments = relationship("Experiment", back_populates="project")


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    parameter = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    log_path = Column(String, unique=True)

    project = relationship("Project", back_populates="experiments")
