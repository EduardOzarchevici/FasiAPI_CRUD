"""fix

Revision ID: c330377bf8d0
Revises: 
Create Date: 2025-07-15 10:46:13.321932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c330377bf8d0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Creează tipul ENUM doar dacă nu există deja
    role_enum = postgresql.ENUM('admin', 'editor', name='roleenum')

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False, index=True),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('age', sa.Integer, nullable=False, index=True),
        sa.Column('role', role_enum, nullable=False, server_default='editor'),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('activated', sa.Boolean, nullable=False, server_default=sa.text('true')),
        sa.Column('password', sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
    role_enum = postgresql.ENUM(name='roleenum')
    role_enum.drop(op.get_bind(), checkfirst=True)