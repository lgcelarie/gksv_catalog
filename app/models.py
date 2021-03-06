from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from app import login

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
    __searchable__ = ['nombre']
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index = True, nullable = False)
    slug = db.Column(db.String(100), nullable = False, unique=True)
    imagen = db.Column(db.String(120), nullable = False)
    productos = db.relationship('Producto', backref='marca', lazy='dynamic')
    def __repr__(self):
        return '<Marca %r>' % self.id

productoCategorias = db.Table('productos_x_categoria',
    db.Column('producto_id', db.Integer, db.ForeignKey('productos.id'), primary_key=True),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categorias.id'), primary_key=True),    
)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    __searchable__ = ['nombre']
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    slug = db.Column(db.String(100), nullable = False, unique=True)
    peq_desc = db.Column(db.String(250))
    imagen = db.Column(db.String(120), nullable = False)
    estado = db.Column(db.Enum(EstadoCatalogo), nullable = False, default = EstadoCatalogo.ACTIVO)
    productos = db.relationship('Producto', secondary=productoCategorias, lazy='subquery',
        backref=db.backref('productos', lazy='dynamic'))
    def __repr__(self):
        return '<Categoria %r>' % self.nombre

class Producto(db.Model):
    __tablename__ = 'productos'
    __searchable__ = ['nombre','peq_desc','descripcion']
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
    categorias = db.relationship('Categoria', secondary=productoCategorias, lazy='subquery',
        backref=db.backref('categorias', lazy='dynamic'))

    def estrellas(self):
        return (int(self.condicion)/2,round(self.condicion%2))

    def __repr__(self):
        return '<Producto %r>' % self.id


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
        

class Administrador(UserMixin, db.Model):
    __tablename__ = "usuarios_admin"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Administrador {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return Administrador.query.get(int(id)) 
        