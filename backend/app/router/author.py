from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.schemas.author import AuthdetayCreate, AuthdetayOut
from app.services.author import (
    create_author, get_author, get_authors,
    update_author, delete_author
)
from app.utils.db_session import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])
templates = Jinja2Templates(directory="templates")

@router.post("/", response_model=AuthdetayOut)
def add_author(author: AuthdetayCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get("/", response_model=list[AuthdetayOut])
def list_authors(db: Session = Depends(get_db)):
    return get_authors(db)

@router.get("/{aid}", response_model=AuthdetayOut)
def read_author(aid: int, db: Session = Depends(get_db)):
    author = get_author(db, aid)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{aid}", response_model=AuthdetayOut)
def edit_author(aid: int, author: AuthdetayCreate, db: Session = Depends(get_db)):
    updated = update_author(db, aid, author)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated

@router.delete("/{aid}")
def remove_author(aid: int, db: Session = Depends(get_db)):
    success = delete_author(db, aid)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}

# ✅ HTML Template route
@router.get("/html/{aid}", response_class=HTMLResponse)
def author_page(request: Request, aid: int, db: Session = Depends(get_db)):
    author = get_author(db, aid)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return templates.TemplateResponse("author.html", {"request": request, "author": author})
