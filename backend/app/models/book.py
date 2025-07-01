from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# 1. BookDetay – temel kitap bilgileri ve sağ kutucuk içeriği
class BookDetay(Base):
    __tablename__ = "bookdetay"

    bid = Column(Integer, primary_key=True, index=True)
    adi = Column(String, nullable=False)
    yazar = Column(String, nullable=False)
    yil = Column(Integer)
    tür = Column(String)
    dil = Column(String)
    ülke = Column(String)
    yayin = Column(String)
    sf = Column(Integer)
    isbn = Column(String)
    bpng = Column(String)    # görsel dosya adı
    burl = Column(String)    # görsel url (gerekirse)

    # İlişki
    desc = relationship("BookDesc", back_populates="detay", uselist=False)
    tree = relationship("BookTree", back_populates="detay", uselist=False)


# 2. BookDesc – wiki metin alanları
class BookDesc(Base):
    __tablename__ = "bookdesc"

    bid = Column(Integer, ForeignKey("bookdetay.bid"), primary_key=True)
    giris = Column(String)
    konu = Column(String)
    icerik = Column(String)
    ayrica = Column(String)
    kaynak = Column(String)

    detay = relationship("BookDetay", back_populates="desc")


# 3. BookTree – basım ve teknik bilgiler
class BookTree(Base):
    __tablename__ = "booktree"

    bid = Column(Integer, ForeignKey("bookdetay.bid"), primary_key=True)
    originadi = Column(String)
    ceviri = Column(String)
    ilkyayin = Column(String)

    detay = relationship("BookDetay", back_populates="tree")
