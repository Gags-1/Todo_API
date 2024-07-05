"""Adding tasks table

Revision ID: 7397dbb296d0
Revises: 62a10020a7de
Create Date: 2024-07-05 00:35:59.073955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7397dbb296d0'
down_revision: Union[str, None] = '62a10020a7de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('task', sa.String, nullable=False),
        sa.Column('completed', sa.Boolean, server_default='FALSE', nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    )



def downgrade() -> None:
    op.drop_table('tasks')
