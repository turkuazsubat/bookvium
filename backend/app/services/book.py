from sqlalchemy.orm import Session
from app.models.book import BookDetay, BookDesc, BookTree
from app.schemas.book import BookDetayCreate
from sqlalchemy.sql import func


def create_book(db: Session, book: BookDetayCreate):
    db_book = BookDetay(**book.model_dict(exclude={"desc", "tree"}))
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    if book.desc:
        db_desc = BookDesc(bid=db_book.bid, **book.desc.model_dict())
        db.add(db_desc)

    if book.tree:
        db_tree = BookTree(bid=db_book.bid, **book.tree.model_dict())
        db.add(db_tree)

    db.commit()
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(BookDetay).filter(BookDetay.bid == book_id).first()

def get_books(db: Session, skip=0, limit=10):
    return db.query(BookDetay).offset(skip).limit(limit).all()

def delete_book(db: Session, book_id: int):
    book = db.query(BookDetay).filter(BookDetay.bid == book_id).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return True

# app/services/book.py
def get_latest_books(db: Session, limit: int = 5):
    return db.query(BookDetay).order_by(BookDetay.id.desc()).limit(limit).all()

def get_random_book(db: Session):
    return db.query(BookDetay).order_by(func.random()).first()

def get_fixed_book(db: Session, id: int):
    return db.query(BookDetay).filter(BookDetay.bid == id).first()

