"""uso de categorias

Revision ID: 6b81d641cb1e
Revises: 951e7e6a57db
Create Date: 2018-11-23 22:43:25.903272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b81d641cb1e'
down_revision = '951e7e6a57db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('peq_desc', sa.String(length=250), nullable=True),
    sa.Column('imagen', sa.String(length=120), nullable=False),
    sa.Column('estado', sa.Enum('ACTIVO', 'INACTIVO', name='estadocatalogo'), nullable=False,
        server_default='ACTIVO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('productos_x_categoria',
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('producto_id', 'categoria_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productos_x_categoria')
    op.drop_table('categorias')
    # ### end Alembic commands ###
