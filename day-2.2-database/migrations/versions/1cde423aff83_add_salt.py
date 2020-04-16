"""add salt

Revision ID: 1cde423aff83
Revises: 1ae759ea899c
Create Date: 2020-04-16 18:37:44.927112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cde423aff83'
down_revision = '1ae759ea899c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('salt', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'salt')
    # ### end Alembic commands ###