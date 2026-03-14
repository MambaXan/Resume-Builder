from sqlalchemy.orm import Session
from . import models, schemas, auth_utils


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_p = auth_utils.get_password_hash(user.password)

    db_user = models.User(
        email=user.email,
        hashed_password=hashed_p
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_resumes(db: Session, user_id: int):
    return db.query(models.Resume).filter(models.Resume.user_id == user_id).all()


def create_user_resume(db: Session, resume: schemas.ResumeCreate, user_id: int):
    db_resume = models.Resume(**resume.dict(), user_id=user_id)

    db.add(db_resume)

    db.commit()

    db.refresh(db_resume)

    return db_resume
