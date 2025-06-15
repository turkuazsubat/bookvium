from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut
from app.services.book import create_book, get_books, get_book, update_book, delete_book
from app.utils.db_session import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=list[BookOut])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.get("/{book_id}", response_model=BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookOut)
def edit_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    updated = update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
