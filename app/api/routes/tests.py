from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.test import TestCreate, TestOut
from app.crud import test as crud_test

router = APIRouter(prefix="/tests", tags=["tests"])

@router.post("", response_model=TestOut, status_code=201)
def create_test(test_in: TestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_test.create(db, owner_id=current_user.id, title=test_in.title, description=test_in.description)

@router.get("/{test_id}", response_model=TestOut)
def get_test(test_id: int, db: Session = Depends(get_db)):
    test = crud_test.get(db, test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

@router.delete("/{test_id}", status_code=204)
def delete_test(
    test_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    test = crud_test.get(db, test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

    # Authorization check
    if test.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    crud_test.delete(db, test)
    return

@router.get("")
def list_tests(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    q: str | None = None,
    sort: str = Query("desc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db),
):
    return crud_test.list_tests(db, skip, limit, q, sort)


