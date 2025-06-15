from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    summary: str | None = None

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True
