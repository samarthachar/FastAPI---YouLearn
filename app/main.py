from fastapi import FastAPI # type: ignore

from app.schemas.user import UserCreate, UserOut


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

