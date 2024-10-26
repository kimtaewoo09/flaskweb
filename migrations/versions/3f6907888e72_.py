"""empty message

Revision ID: 3f6907888e72
Revises: 3d01e6b0683b
Create Date: 2024-10-24 17:12:54.621817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6907888e72'
down_revision = '3d01e6b0683b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_number')
        batch_op.drop_column('number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number', sa.VARCHAR(), nullable=True))
        batch_op.create_index('ix_users_number', ['number'], unique=False)

    # ### end Alembic commands ###