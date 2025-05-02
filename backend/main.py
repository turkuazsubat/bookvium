from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Bookvium")

app.include_router(router)
