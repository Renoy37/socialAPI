"""add content column to post table 

Revision ID: 1cc3db8c4690
Revises: 4e4309604b0b
Create Date: 2023-10-18 10:36:49.414643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cc3db8c4690'
down_revision: Union[str, None] = '4e4309604b0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
