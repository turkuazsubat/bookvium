from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryOut
from app.services.category import create_category, get_category, get_categories
from app.utils.db_session import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryOut)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    return create_category(db, category)

@router.get("/", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
