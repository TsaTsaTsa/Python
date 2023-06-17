"""Creation6

Revision ID: be8e33092282
Revises: 23b3512f88a9
Create Date: 2023-06-17 14:26:10.409272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be8e33092282'
down_revision = '23b3512f88a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('playlist_songs_fkey', 'playlist', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('playlist_songs_fkey', 'playlist', 'song', ['songs'], ['id'])
    # ### end Alembic commands ###
