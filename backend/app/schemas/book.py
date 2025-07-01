from pydantic import BaseModel
from typing import Optional

# 1. BookTree
class BookTreeBase(BaseModel):
    originadi: Optional[str] = None
    ceviri: Optional[str] = None
    ilkyayin: Optional[str] = None

class BookTreeCreate(BookTreeBase):
    pass

class BookTreeOut(BookTreeBase):
    class Config:
        from_attributes = True


# 2. BookDesc
class BookDescBase(BaseModel):
    giris: Optional[str] = None
    konu: Optional[str] = None
    icerik: Optional[str] = None
    ayrica: Optional[str] = None
    kaynak: Optional[str] = None

class BookDescCreate(BookDescBase):
    pass

class BookDescOut(BookDescBase):
    class Config:
        from_attributes = True


# 3. BookDetay (ana model)
class BookDetayBase(BaseModel):
    adi: str
    yazar: str
    yil: Optional[int] = None
    tür: Optional[str] = None
    dil: Optional[str] = None
    ülke: Optional[str] = None
    yayin: Optional[str] = None
    sf: Optional[int] = None
    isbn: Optional[str] = None
    bpng: Optional[str] = None
    burl: Optional[str] = None

class BookDetayCreate(BookDetayBase):
    desc: Optional[BookDescCreate] = None
    tree: Optional[BookTreeCreate] = None

class BookDetayOut(BookDetayBase):
    bid: int
    desc: Optional[BookDescOut] = None
    tree: Optional[BookTreeOut] = None

    class Config:
        from_attributes = True