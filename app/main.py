from fastapi import FastAPI, Depends # type: ignore
from sqlalchemy.orm import Session 

from app.schemas.user import UserCreate, UserOut
from app.api.deps import get_db



app = FastAPI(title="Test API", version="0.1.0")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/version")
def get_version():
    return {"version": "0.1.0"}

@app.post("/debug/users")
def debug_user(user: UserCreate):
    return {"ok": True, "parsed": user.model_dump(exclude={"password"})}

@app.get("/test-user", response_model=UserOut)
def test_user():
    return { "id": 1, "email": "test@example.com", "full_name": "Test User", "debug": "x" }

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    print("DB session type:", type(db))
    return {"session type": str(type(db))}
