"""add phone_number and user_info to table

Revision ID: 74ee00e766e8
Revises: 78c92104bc16
Create Date: 2023-10-19 08:14:26.875615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74ee00e766e8'
down_revision: Union[str, None] = '78c92104bc16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    op.add_column('users', sa.Column('user_info', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_info')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
