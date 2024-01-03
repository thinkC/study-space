# from pydantic import BaseModel, EmailStr
# from pydantic import BaseModel as PydanticBaseModel
# from datetime import date, datetime, time, timedelta
# from typing import Optional


# class Config:
#     arbitrary_types_allowed = True


# class BaseModel(PydanticBaseModel):
#     class Config:
#         arbitrary_types_allowed = True
# # moved up
# # customise server reponse for user


# class Create_User_Reponse(BaseModel):
#     firstname: str
#     lastname: str
#     email: EmailStr
#     user_id: int
#     created_at: datetime


# # convert sqlalcamey model to a pydantic model


#     class Config:
#         orm_mode = True


# class Create_Space_User(BaseModel):
#     booking_date: datetime
#     booking_start_time: time
#     booking_end_time: time
#     study_space_number: int
#     number_of_seats: int
#     email: str
#     # user_id: int
#     study_room_id: int
#     user: Optional[Create_User_Reponse]  # just added


# class Create_Space_Admin(BaseModel):
#     study_space_number: int
#     number_of_seats: int
#     library_name: str


# class Create_User(BaseModel):
#     firstname: str
#     lastname: str
#     password: str
#     email: EmailStr


# class Create_Space_User_Response(Create_Space_User):
#     user_id: int
#     user: Create_User_Reponse  # just added

#     class Config:
#         orm_mode = True
# # was working
# # # customise server reponse for user


# # class Create_User_Reponse(BaseModel):
# #     firstname: str
# #     lastname: str
# #     email: EmailStr
# #     user_id: int
# #     created_at: datetime


# # # convert sqlalcamey model to a pydantic model

# #     class Config:
# #         orm_mode = True

# # end of was working
# # Loin schema


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

# # for token


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     id: Optional[int] = None


# before adding "user" used in models for relationship


from pydantic import BaseModel, EmailStr
from pydantic import BaseModel as PydanticBaseModel
from datetime import date, datetime, time, timedelta
from typing import Optional


class Config:
    arbitrary_types_allowed = True


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Create_Space_User(BaseModel):
    booking_date: datetime
    booking_start_time: time
    booking_end_time: time
    study_space_number: int
    number_of_seats: int
    email: str
    # user_id: int
    study_room_id: int


class Create_Space_Admin(BaseModel):
    study_space_number: int
    number_of_seats: int
    library_name: str


class Create_User(BaseModel):
    firstname: str
    lastname: str
    password: str
    email: EmailStr


class Create_Space_User_Response(Create_Space_User):
    user_id: int

    class Config:
        orm_mode = True

# customise server reponse for user


class Create_User_Reponse(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    user_id: int
    created_at: datetime


# convert sqlalcamey model to a pydantic model


    class Config:
        orm_mode = True

# Loin schema


class UserLogin(BaseModel):
    email: EmailStr
    password: str

# for token


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
