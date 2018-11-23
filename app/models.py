from werkzeug.security import generate_password_hash, check_password_hash
from . import db

import enum
class EstadoProducto(enum.Enum):
    DISPONIBLE = 'DISPONIBLE'
    RESERVADO = 'RESERVADO'
    AGOTADO = 'AGOTADO'

class EstadoCatalogo(enum.Enum):
    ACTIVO = 'ACTIVO'
    INACTIVO = 'INACTIVO'

class Marca(db.Model):
    __tablename__ = 'marcas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index = True, nullable = False)
    productos = db.relationship('Producto', backref='marca', lazy='dynamic')
    def __repr__(self):
        return '<Marca %r>' % self.id

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    peq_desc = db.Column(db.String(250))
    imagen = db.Column(db.String(120), nullable = False)
    estado = db.Column(db.Enum(Marca), nullable = False, default = EstadoCatalogo.ACTIVO)
    def __repr__(self):
        return '<Categoria %r>' % self.nombre

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(100), nullable = False, unique=True)
    nombre = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.Enum(EstadoProducto), nullable = False)
    condicion = db.Column(db.Float, nullable = False, default= '0.0')
    cant_visto = db.Column(db.Integer, nullable = False, default = 0)
    peq_desc = db.Column(db.String(250))
    descripcion = db.Column(db.Text, nullable = False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'))
    imagenes = db.relationship('Imagen', backref='producto', lazy='dynamic')
    visitas = db.relationship('Visita', backref='producto', lazy='dynamic')

    def __repr__(self):
        return '<Producto %r>' % self.id

class ProductoCategoria(db.Model):
    __tablename__ = 'productos_x_categoria'
    id = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))

    def __repr__(self):
        return '<ProductoCategoria %r>' % self.id

class Imagen(db.Model):
    __tablename__ = 'imagenes'
    id = db.Column(db.Integer, primary_key = True)
    primaria = db.Column(db.Boolean, nullable = False)
    ruta = db.Column(db.String(120), nullable = False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))

    def __repr__(self):
        return '<Imagen %r>' % self.id



class Visita(db.Model):
    __tablename__ = 'visitas'
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.String(15), nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))

    def __repr__(self):
        return '<Visita %r>' % self.id
        