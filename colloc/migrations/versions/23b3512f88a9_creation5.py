"""Creation5

Revision ID: 23b3512f88a9
Revises: 7bdf1173a2b7
Create Date: 2023-06-17 13:49:37.241383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23b3512f88a9'
down_revision = '7bdf1173a2b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('album', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('song', 'album')
    # ### end Alembic commands ###