from fastapi import APIRouter
from app.schemas import Book
from app.services import get_books, add_book

router = APIRouter()

@router.get("/")
def index():
    return {"message": "Welcome to Bookvium API"}

@router.get("/books")
def list_books():
    return get_books()

@router.post("/books")
def create_book(book: Book):
    return add_book(book)
