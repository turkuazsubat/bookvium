from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

from sqlalchemy import asc, desc

def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        summary=book.summary,
        publication_year=book.publication_year,
        category_id=book.category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, order_by: str = None, order_dir: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(Book)

    if order_by:

        valid_order_fields = ["title", "author", "id", "publication_year"]
        if order_by not in valid_order_fields:
            order_by = "id"
        
        direction = asc if order_dir.lower() == "asc" else desc
        column = getattr(Book, order_by)
        query = query.order_by(direction(column))

    return query.offset(skip).limit(limit).all()

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

def search_books(db: Session, title: str = None, author: str = None, category_id: int = None, order_by: str = None, order_dir: str = "asc", skip: int = 0, limit: int = 10):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if category_id:
        query = query.filter(Book.category_id == category_id)
    if order_by:
        
        valid_order_fields = ["title", "author", "id", "publication_year"]
        if order_by not in valid_order_fields:
            order_by = "id"
        direction = asc if order_dir.lower() == "asc" else desc
        column = getattr(Book, order_by)
        query = query.order_by(direction(column))

    return query.offset(skip).limit(limit).all()

