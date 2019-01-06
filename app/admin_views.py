from flask_admin import BaseView, expose
from sqlalchemy.sql import text
from . import db


class DashboardView(BaseView):
    @expose('/')
    def index(self):
        productos = db.engine.execute(text('select productos.id, productos.nombre, count(visitas.id) from productos join visitas on productos.id = visitas.producto_id where date(visitas.fecha) = date(CURDATE()) GROUP BY productos.id'))
        return self.render('admin/index.html',productos=productos)