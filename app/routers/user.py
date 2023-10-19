from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import models, schemas, utilities
from ..database import Session, get_db

router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def Create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hashing the password
    hashed_password = utilities.hash(user.password)
    user.password = hashed_password

    new_user = models.User(** user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db),):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id:{id} does not exist")

    return user
