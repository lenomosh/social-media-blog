"""empty message

Revision ID: 6f43a0270a65
Revises: 3a1840242007
Create Date: 2020-10-01 11:53:20.408744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f43a0270a65'
down_revision = '3a1840242007'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'title')
    # ### end Alembic commands ###