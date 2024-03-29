"""create_users_table

Revision ID: 15fcb3f62d8c
Revises: 
Create Date: 2024-01-03 14:35:26.301022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15fcb3f62d8c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('study_rooms',
    sa.Column('study_room_id', sa.Integer(), nullable=False),
    sa.Column('study_space_number', sa.Integer(), nullable=False),
    sa.Column('number_of_seats', sa.Integer(), nullable=False),
    sa.Column('library_name', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('study_room_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('study_spaces',
    sa.Column('study_space_id', sa.Integer(), nullable=False),
    sa.Column('study_space_number', sa.Integer(), nullable=False),
    sa.Column('number_of_seats', sa.Integer(), nullable=False),
    sa.Column('booking_date', sa.Date(), nullable=False),
    sa.Column('booking_start_time', sa.Time(), nullable=False),
    sa.Column('booking_end_time', sa.Time(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('study_room_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['study_room_id'], ['study_rooms.study_room_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('study_space_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('study_spaces')
    op.drop_table('users')
    op.drop_table('study_rooms')
    # ### end Alembic commands ###
