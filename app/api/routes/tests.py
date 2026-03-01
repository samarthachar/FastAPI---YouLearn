from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.test import TestCreate, TestOut
from app.crud import test as crud_test

router = APIRouter(prefix="/tests", tags=["tests"])

@router.post("", response_model=TestOut, status_code=201)
def create_test(test_in: TestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # TEMP: hardcode owner_id until auth is added
    return crud_test.create(db, owner_id=1, title=test_in.title, description=test_in.description)

@router.get("/{test_id}", response_model=TestOut)
def get_test(test_id: int, db: Session = Depends(get_db)):
    test = crud_test.get(db, test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

