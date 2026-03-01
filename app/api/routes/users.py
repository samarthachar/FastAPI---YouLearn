from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.user import UserCreate, UserOut
from app.crud import user as crud_user
from app.core.security import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserOut, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    if user_in.full_name == "admin":
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Title 'admin' is not allowed.", 
        )
    return crud_user.create(db, email=user_in.email, full_name=user_in.full_name, hashed_password=get_password_hash(user_in.password))

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    test = crud_user.get(db, user_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test



@router.get("/me")
def read_me(current_user = Depends(get_current_user)):
    return current_user
