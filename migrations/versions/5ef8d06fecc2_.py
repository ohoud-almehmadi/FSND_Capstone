"""empty message

Revision ID: 5ef8d06fecc2
Revises: 
Create Date: 2021-09-26 23:29:17.453016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ef8d06fecc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('date', sa.String(), nullable=True))
    op.drop_column('movies', 'release_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('release_date', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('movies', 'date')
    # ### end Alembic commands ###