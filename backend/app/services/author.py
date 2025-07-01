from sqlalchemy.orm import Session
from app.models.author import Authdetay, AuthDesc
from app.schemas.author import AuthdetayCreate
from sqlalchemy.sql import func

def create_author(db: Session, author: AuthdetayCreate):
    db_author = Authdetay(**author.dict(exclude={"desc"}))
    if author.desc:
        db_desc = AuthDesc(**author.desc.dict())
        db_author.desc = db_desc
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, aid: int):
    return db.query(Authdetay).filter(Authdetay.aid == aid).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Authdetay).offset(skip).limit(limit).all()

def delete_author(db: Session, aid: int):
    author = get_author(db, aid)
    if author:
        db.delete(author)
        db.commit()
        return True
    return False

def update_author(db: Session, aid: int, author_data: AuthdetayCreate):
    author = get_author(db, aid)
    if not author:
        return None
    for field, value in author_data.dict(exclude_unset=True, exclude={"desc"}).items():
        setattr(author, field, value)
    if author_data.desc:
        for field, value in author_data.desc.dict(exclude_unset=True).items():
            setattr(author.desc, field, value)
    db.commit()
    db.refresh(author)
    return author

# app/services/author.py
def get_latest_authors(db: Session, limit: int = 5):
    return db.query(Authdetay).order_by(Authdetay.aid.desc()).limit(limit).all()

def get_random_author(db: Session):
    return db.query(Authdetay).order_by(func.random()).first()
