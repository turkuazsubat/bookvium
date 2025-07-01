# app/schemas/author.py
from pydantic import BaseModel
from typing import Optional

class AuthDescBase(BaseModel):
    giris: Optional[str] = None
    yasam: Optional[str] = None
    eser: Optional[str] = None
    ayrica: Optional[str] = None

class AuthDescCreate(AuthDescBase):
    pass

class AuthDescOut(AuthDescBase):
    class Config:
        from_attributes = True


class AuthdetayBase(BaseModel):
    adi: str
    dogum: Optional[str] = None
    ulke: Optional[str] = None
    dil: Optional[str] = None
    tür: Optional[str] = None
    akim: Optional[str] = None
    meslek: Optional[str] = None
    onemli: Optional[str] = None
    apng: Optional[str] = None
    aurl: Optional[str] = None

class AuthdetayCreate(AuthdetayBase):
    desc: Optional[AuthDescCreate] = None

class AuthdetayOut(AuthdetayBase):
    aid: int
    desc: Optional[AuthDescOut] = None

    class Config:
        from_attributes = True
