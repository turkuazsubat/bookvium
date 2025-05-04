from fastapi import FastAPI
from app.router import router
from app import config

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
app.include_router(router)
