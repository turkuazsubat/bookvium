from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut
from app.services.book import create_book, get_books, get_book, update_book, delete_book, search_books
from app.utils.db_session import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=list[BookOut])
def read_books(
    title: str = Query(default=None, description="Kitap başlığı"),
    author: str = Query(default=None, description="Yazar adı"),
    category_id: int = Query(default=None, description="Kategori ID"),
    order_by: str = Query(default=None, description="Sıralama alanı (title, author, id, publication_year)"),
    order_dir: str = Query(default="asc", description="Sıralama yönü: asc veya desc"),
    skip: int = Query(default=0, ge=0, description="Kaç kayıt atlanacak"),
    limit: int = Query(default=10, ge=1, le=100, description="Maksimum kayıt sayısı"),
    db: Session = Depends(get_db)
):
    if title or author or category_id:
        return search_books(
            db,
            title=title,
            author=author,
            category_id=category_id,
            order_by=order_by,
            order_dir=order_dir,
            skip=skip,
            limit=limit
        )
    return get_books(
        db,
        order_by=order_by,
        order_dir=order_dir,
        skip=skip,
        limit=limit
    )

@router.get("/", response_model=list[BookOut])
def read_books(
    title: str = Query(default=None),
    author: str = Query(default=None),
    category_id: int = Query(default=None),
    db: Session = Depends(get_db)
):
    if title or author or category_id:
        return search_books(db, title=title, author=author, category_id=category_id)
    return get_books(db)


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
