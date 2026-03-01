from fastapi import FastAPI
from app.api.routes import tests
from app.api.routes import users
from app.api.routes import auth

from app.db.base import Base
from app.db.session import engine
from app.models import test  # IMPORTANT: import models before create_all


app = FastAPI(title="Test API", version="0.1.0")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(tests.router)
app.include_router(users.router)
app.include_router(auth.router)