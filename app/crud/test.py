from sqlalchemy.orm import Session
from app.models.test import Test
from app.schemas.test import TestUpdate

def create(db: Session, *, owner_id: int, title: str, description: str | None = None) -> Test:
    test = Test(owner_id=owner_id, title=title, description=description)

    db.add(test)
    db.commit()
    db.refresh(test)
    return test

def get(db: Session, test_id: int) -> Test | None:
    return db.query(Test).filter(Test.id == test_id).first()

def list(db: Session, *, skip: int = 0, limit: int = 20) -> list[Test]: # type: ignore
    return db.query(Test).offset(skip).limit(limit).all()

def update(db: Session, db_obj: Test, obj_in: TestUpdate) -> Test:
    update_data = obj_in.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
