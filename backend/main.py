from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import config
from app.database import Base, engine
from app.models.book import Book  # Veritabanı modeli

# Router'ları import et
from app.router import router
from app.router.book import router as book_router
from app.router.category import router as category_router
from app.router.user import router as user_router
from app.router.auth import router as auth_router  # Eksik olan buydu

from app.router.author import router as author_router

from app.router import main as main_router

# FastAPI uygulamasını başlat
app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

# HTML template klasörünü tanımla
templates = Jinja2Templates(directory="frontend/templates")

# =================== FRONTEND ROUTES ===================

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/book/{book_id}", response_class=HTMLResponse)
async def book_detail_page(book_id: int, request: Request):
    return templates.TemplateResponse("book.html", {"request": request, "book_id": book_id})

@app.get("/author/{author_id}", response_class=HTMLResponse)
async def author_detail_page(author_id: int, request: Request):
    return templates.TemplateResponse("author.html", {"request": request, "author_id": author_id})

@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/404", response_class=HTMLResponse)
async def not_found_page(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})

# =================== BACKEND API ROUTES ===================

app.include_router(router)
app.include_router(book_router)
app.include_router(category_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(author_router)
app.include_router(main_router)

