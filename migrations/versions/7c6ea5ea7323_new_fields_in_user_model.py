"""new fields in user model

Revision ID: 7c6ea5ea7323
Revises: ff47d2fa0796
Create Date: 2022-01-18 17:35:09.796078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c6ea5ea7323'
down_revision = 'ff47d2fa0796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'last_seen')
    op.drop_column('post', 'about_me')
    # ### end Alembic commands ###