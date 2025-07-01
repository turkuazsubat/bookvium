from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas.book import BookDetayCreate, BookDetayOut
from app.services.book import create_book, get_book, get_books, delete_book
from app.utils.db_session import get_db

router = APIRouter(prefix="/books", tags=["Books"])
templates = Jinja2Templates(directory="frontend/templates")

@router.post("/", response_model=BookDetayOut)
def create(book: BookDetayCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/{book_id}", response_class=HTMLResponse)
def read_book(book_id: int, request: Request, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return templates.TemplateResponse("book.html", {"request": request, "book": book})
