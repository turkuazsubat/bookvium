from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# 1. Açıklama: Giriş, Yaşam, Eserleri, Ayrıca
class AuthDesc(Base):
    __tablename__ = "authdesc"

    aid = Column(Integer, ForeignKey("authdetay.aid"), primary_key=True)
    giris = Column(String)
    yasam = Column(String)
    eser = Column(String)
    ayrica = Column(String)

    detay = relationship("Authdetay", back_populates="desc")

# 2. Ana yazar tablosu
class Authdetay(Base):
    __tablename__ = "authdetay"

    aid = Column(Integer, primary_key=True, index=True)
    adi = Column(String, nullable=False)
    dogum = Column(String)
    ulke = Column(String)
    dil = Column(String)
    tür = Column(String)
    akim = Column(String)
    meslek = Column(String)
    onemli = Column(String)
    apng = Column(String)
    aurl = Column(String)

    desc = relationship("AuthDesc", back_populates="detay", uselist=False, cascade="all, delete-orphan")
