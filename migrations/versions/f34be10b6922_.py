"""empty message

Revision ID: f34be10b6922
Revises: 63187d1e1ae8
Create Date: 2024-09-21 10:45:27.130248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f34be10b6922'
down_revision = '63187d1e1ae8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_userid')
        batch_op.drop_column('userid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.VARCHAR(), nullable=True))
        batch_op.create_index('ix_users_userid', ['userid'], unique=False)

    # ### end Alembic commands ###