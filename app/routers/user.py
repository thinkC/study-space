from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from .. database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# User route

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Create_User_Reponse)
def create_user(user: schemas.Create_User, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # hash password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Create_User_Reponse)
# def create_user(user: schemas.Create_User, db: Session = Depends(get_db)):

#     # hash password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


@router.get("/{id}", response_model=schemas.Create_User_Reponse)
def get_user(id: int, db: Session = Depends(get_db),):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"space booking with id {id} not found")
    return user
