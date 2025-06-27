from fastapi import FastAPI
from app import config

from app.database import Base, engine
from app.models.book import Book  # Veritabanı modeli

# Router'ları import et
from app.router import router
from app.router.book import router as book_router
from app.router.category import router as category_router
from app.router.user import router as user_router
from app.router.auth import router as auth_router  # Eksik olan buydu

# FastAPI uygulamasını başlat
app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

# Ana router (genel)
app.include_router(router)

# Kitaplar için router
app.include_router(book_router)

# Kategoriler için router
app.include_router(category_router)

# Kimlik doğrulama ve kullanıcı işlemleri için router'lar
app.include_router(auth_router)
app.include_router(user_router)
