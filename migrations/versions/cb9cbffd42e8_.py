"""empty message

Revision ID: cb9cbffd42e8
Revises: f76551d165db
Create Date: 2019-01-13 21:12:55.925959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb9cbffd42e8'
down_revision = 'f76551d165db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios_admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('usuarios_admin', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_usuarios_admin_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios_admin', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usuarios_admin_email'))

    op.drop_table('usuarios_admin')
    # ### end Alembic commands ###