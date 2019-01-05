from flask_admin import BaseView, expose
from . import db


class DashboardView(BaseView):
    @expose('/')
    def index(self):
        productos = db.session.execute('select productos.*, count(visitas.id) from productos join visitas on productos.id = visitas.producto_id where date(visitas.fecha) = date(CURDATE()) GROUP BY productos.id')
        return self.render('admin/index.html',productos=productos)