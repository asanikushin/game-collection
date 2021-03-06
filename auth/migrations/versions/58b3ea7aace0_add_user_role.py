"""add user role

Revision ID: 58b3ea7aace0
Revises: 6208cacc42b5
Create Date: 2020-04-18 11:49:19.561754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "58b3ea7aace0"
down_revision = "6208cacc42b5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("role", sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "role")
    # ### end Alembic commands ###
