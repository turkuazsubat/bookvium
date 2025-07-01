from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.utils.db_session import get_db
from app.services.book import get_random_book, get_latest_books
from app.services.author import get_latest_authors, get_random_author

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", include_in_schema=False)
def homepage(request: Request, db: Session = Depends(get_db)):
    featured_book = get_latest_books(db, 1)[0] if get_latest_books(db, 1) else None
    featured_author = get_latest_authors(db, 1)[0] if get_latest_authors(db, 1) else None
    latest_book = get_latest_books(db, 1)[0] if get_latest_books(db, 1) else None
    random_book = get_random_book(db)

    return templates.TemplateResponse("main.html", {
        "request": request,
        "featured_book": featured_book,
        "featured_author": featured_author,
        "latest_book": latest_book,
        "random_book": random_book
    })
