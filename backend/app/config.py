from dotenv import load_dotenv
from pathlib import Path
import os

# backend/.env dosyasını bulur
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

PROJECT_NAME = os.getenv("PROJECT_NAME")
VERSION = os.getenv("VERSION")

