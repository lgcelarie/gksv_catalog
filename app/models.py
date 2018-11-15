from werkzeug.security import generate_password_hash, check_password_hash
from SQLAlchemy


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.Enum({}))
    cant_visto = db.Column(db.Integer)
    peq_desc = db.Column(sb.String(244))
    descripcion = db.Column()
    marca_id = db.Column()


