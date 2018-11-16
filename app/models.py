from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Marca(db.Model):
    __tablename__ = 'marcas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index = True)
    productos = db.relationship('Producto', backref='marca', lazy='dynamic')
    def __repr__(self):
        return '<Marca %r>' % self.id


class Imagen(db.Model):
    __tablename__ = 'imagenes'
    id = db.Column(db.Integer, primary_key = True)
    primaria = db.Column(db.Boolean)
    ruta = db.Column(db.String(120))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))

    def __repr__(self):
        return '<Imagen %r>' % self.id



class Visita(db.Model):
    __tablename__ = 'visitas'
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.String(15))
    fecha = db.Column(db.DateTime)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))

    def __repr__(self):
        return '<Visita %r>' % self.id
        

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.Enum(('Disponible', 'Reservado', 'Agotado')))
    cant_visto = db.Column(db.Integer)
    peq_desc = db.Column(db.String(250))
    descripcion = db.Column(db.Text)
    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'))
    imagenes = db.relationship('Imagen', backref='producto', lazy='dynamic')
    visitas = db.relationship('Visita', backref='producto', lazy='dynamic')

    def __repr__(self):
        return '<Producto %r>' % self.id