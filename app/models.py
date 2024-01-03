from sqlalchemy import text, TIMESTAMP, Column, Integer, String, Date, Time, ForeignKey
# from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKeyConstraint
from .database import Base


class Study_Space(Base):
    __tablename__ = "study_spaces"
    study_space_id = Column(Integer, primary_key=True, nullable=False)
    study_space_number = Column(Integer, nullable=False)
    number_of_seats = Column(Integer, nullable=False)
    booking_date = Column(Date, nullable=False)
    booking_start_time = Column(Time, nullable=False)
    booking_end_time = Column(Time, nullable=False)
    email = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"),
                     nullable=False)  # Reference the users table
    # Reference the study_rooms table
    study_room_id = Column(Integer, ForeignKey(
        "study_rooms.study_room_id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    # Define the relationships for easy querying
    user = relationship("User", back_populates="study_spaces")
    study_room = relationship("Study_Room", back_populates="study_spaces")

# Add this relationship in the User and Study_Room classes as well


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    # Define the relationship for easy querying
    study_spaces = relationship("Study_Space", back_populates="user")


class Study_Room(Base):
    __tablename__ = "study_rooms"
    study_room_id = Column(Integer, primary_key=True, nullable=False)
    study_space_number = Column(Integer, nullable=False)
    number_of_seats = Column(Integer, nullable=False)
    library_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    # Define the relationship for easy querying
    study_spaces = relationship("Study_Space", back_populates="study_room")
