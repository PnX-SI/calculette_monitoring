"""Create schema for module calculatrice

Revision ID: b6e0860c99b8
Create Date: 2025-08-28 10:56:48.006823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e0860c99b8'
down_revision = None
branch_labels = ('calculatrice', )
depends_on = None


def upgrade():
    op.execute(f'CREATE SCHEMA gn_calculatrice')


def downgrade():
    op.execute(f'DROP SCHEMA gn_calculatrice')
