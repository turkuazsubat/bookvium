from pydantic import BaseModel
from app.schemas.category import CategoryOut

class BookBase(BaseModel):
    title: str
    author: str
    summary: str | None = None
    publication_year: int | None = None

class BookCreate(BookBase):
    category_id: int

class BookOut(BookBase):
    id: int
    category: CategoryOut | None = None

    class Config:
        orm_mode = True


