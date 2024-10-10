"""empty message

Revision ID: 3d01e6b0683b
Revises: c0ad9a1e72b6
Create Date: 2024-10-10 17:19:43.256165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d01e6b0683b'
down_revision = 'c0ad9a1e72b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number', sa.String(), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_number'), ['number'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_number'))
        batch_op.drop_column('number')

    # ### end Alembic commands ###
