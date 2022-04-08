from sqlalchemy.orm import Session

import schemas
import dataset_models
import security


def authenticate_user(db, email: str, password: str):
    user = db.query(dataset_models.User).filter(dataset_models.User.email == email).first()
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user
    

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = dataset_models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(dataset_models.User).filter(dataset_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(dataset_models.User).filter(dataset_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dataset_models.User).offset(skip).limit(limit).all()