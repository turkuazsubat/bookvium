from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

def create_book(db: Session, book: BookCreate):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: BookCreate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    for field, value in book_data.dict().items():
        setattr(book, field, value)
    db.commit()
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book
