"""migracion inicial

Revision ID: 1cccba7f33e9
Revises: 
Create Date: 2018-11-16 21:04:57.556707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cccba7f33e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marcas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_marcas_nombre'), 'marcas', ['nombre'], unique=False)
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.Enum('DISPONIBLE', 'RESERVADO', 'AGOTADO', name='estadoproducto'), nullable=False),
    sa.Column('cant_visto', sa.Integer(), nullable=False),
    sa.Column('peq_desc', sa.String(length=250), nullable=True),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['marca_id'], ['marcas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('imagenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primaria', sa.Boolean(), nullable=False),
    sa.Column('ruta', sa.String(length=120), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visitas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=15), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitas')
    op.drop_table('imagenes')
    op.drop_table('productos')
    op.drop_index(op.f('ix_marcas_nombre'), table_name='marcas')
    op.drop_table('marcas')
    # ### end Alembic commands ###