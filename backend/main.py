from fastapi import FastAPI
from app.router import router
from app import config

from app.models.book import Book
from app.database import Base,engine

from app.router.book import router as book_router

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)


Base.metadata.create_all(bind=engine)

app.include_router(router)

app.include_router(book_router)

