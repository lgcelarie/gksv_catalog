from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.sql import text
from . import db

class GKModelView(ModelView):
	def is_accesible(self):
		return login.current_user.is_authenticated
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('main.login', next=request.url))

class DashboardView(AdminIndexView):
    @expose('/')
    def index(self):
        productos = db.engine.execute(text('select productos.id, productos.nombre, count(visitas.id) from productos join visitas on productos.id = visitas.producto_id where date(visitas.fecha) = date(CURDATE()) GROUP BY productos.id'))
        return self.render('admin/dashboard.html',productos=productos)


class ProductoView(GKModelView):
	column_searchable_list = ['nombre', 'peq_desc', 'descripcion']


class MarcaView(GKModelView):
	column_searchable_list = ['nombre']


class CategoriaView(GKModelView):
	column_searchable_list = ['nombre', 'peq_desc']
		