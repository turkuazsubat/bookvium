from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def verify_user_credentials(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
