"""empty message

Revision ID: 25e4e9686313
Revises: 03bf4a8279fa
Create Date: 2023-12-13 11:40:46.515527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25e4e9686313'
down_revision: Union[str, None] = '03bf4a8279fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
