from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import models, schemas, oauth2
from .. database import get_db

# add router

router = APIRouter(
    tags=["Spaces"]
)

# Library spaces route
# @app.get("/spaces_admin")
# def get_posts():
#     return {"data": study_spaces_array}


@router.get("/spaces", response_model=List[schemas.Create_Space_User_Response])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM study_spaces """)
    # posts = cursor.fetchall()
    posts = db.query(models.Study_Space).filter(
        models.Study_Space.email.contains(search)).limit(limit).offset(skip).all()
    # print(current_user.email)
    print(limit)
    # print(posts)
    # return {"data": posts}
    return posts


# @app.post("/spaces_admin", status_code=status.HTTP_201_CREATED)
# def create_study_spaces(post: Create_Space_Admin):
#     # print(post)
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000000)
#     study_spaces_array.append(post_dict)
#     return {"data": post_dict}

@router.post("/spaces_admin", status_code=status.HTTP_201_CREATED)
def create_study_spaces(post: schemas.Create_Space_Admin, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # print(post)
    # post_dict = post.dict()
    # post_dict["id"] = randrange(0, 1000000)
    # study_spaces_array.append(post_dict)

    # new_post = models.Study_Room(study_space_number=post.study_space_number,
    #                              number_of_seats=post.number_of_seats, library_name=post.library_name)

    print(current_user.email)
    new_post = models.Study_Room(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # return {"data": new_post}
    return new_post


@router.post("/spaces", status_code=status.HTTP_201_CREATED, response_model=schemas.Create_Space_User_Response)
def create_study_spaces(post: schemas.Create_Space_User, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    # print(post)
    print(current_user)
    new_post = models.Study_Space(user_id=current_user.user_id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # return {"data": new_post}
    return new_post

# get admin created space


@router.get("/admin_created_space/{id}")
def get_admin_created_space(id):
    print(id)
    return {"post detail": f"this is the id: {id}"}

# get user booked space


# or call it room-booking
@router.get("/spaces/{id}", response_model=schemas.Create_Space_User_Response)
def get_space_booking(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """ SELECT * FROM study_spaces WHERE study_space_id = %s """, (str(id),))
    # space_booking = cursor.fetchone()
    space_booking = db.query(models.Study_Space).filter(
        models.Study_Space.study_space_id == id).first()
    if not space_booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"space booking with id {id} not found")
    # return {"post detail": space_booking}
    return space_booking


# delete
@router.delete("/spaces/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_space_booking(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """DELETE FROM study_spaces WHERE study_space_id = %s returning *""", (str(id),))
    # deleted_space = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Study_Space).filter(
        models.Study_Space.study_space_id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"space booking with id {id} not found")
    # allow only owner of space to delete study space
    if post.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update


@router.put("/spaces/{id}")
def update_space_booking(id: int, updated_post: schemas.Create_Space_User, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """ UPDATE study_spaces SET study_space_number = %s,number_of_seats = %s,
    #     booking_date = %s,booking_start_time = %s, booking_end_time = %s,  email = %s,
    #     user_id = %s, study_room_id = %s WHERE study_space_id = %s RETURNING * """,
    #     (post.study_space_number, post.number_of_seats, post.booking_date,
    #      post.booking_start_time, post.booking_end_time, post.email, post.user_id, post.study_room_id, str(id),))
    # updated_space = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Study_Space).filter(
        models.Study_Space.study_space_id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"space booking with id {id} not found")

    # allow only owner of space to update study space
    if post.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    # return {"data": post_query.first()}
    return post_query.first()


# update study rooms for admins

@router.put("/spaces_admin/{id}")
def update_space_admin(id: int, updated_post: schemas.Create_Space_Admin, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Study_Room).filter(
        models.Study_Room.study_room_id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"space booking with id {id} not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
