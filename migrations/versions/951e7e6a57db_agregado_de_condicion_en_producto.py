"""agregado de condicion en producto

Revision ID: 951e7e6a57db
Revises: 1cccba7f33e9
Create Date: 2018-11-17 20:57:42.952095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '951e7e6a57db'
down_revision = '1cccba7f33e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productos', sa.Column('condicion', sa.Float(), nullable=False, server_default="0.0"))
    op.add_column('productos', sa.Column('slug', sa.String(length=100), nullable=False, server_default=""))
    op.create_unique_constraint(None, 'productos', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'productos', type_='unique')
    op.drop_column('productos', 'slug')
    op.drop_column('productos', 'condicion')
    # ### end Alembic commands ###