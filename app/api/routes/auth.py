from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud.user import get_by_email, create
from app.core.security import get_password_hash, verify_password, create_access_token
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing = get_by_email(db, email=user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = create(db, email=user.email, full_name=user.full_name, hashed_password=get_password_hash(user.password))


    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", status_code=201)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_by_email(db, email=form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password): #type: ignore
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(user.email) #type: ignore

    return {"access_token": token, "token_type": "bearer"}
