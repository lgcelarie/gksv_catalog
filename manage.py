#!/usr/bin/env python
import os
from app import create_app, db
from app import models
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_msearch import Search
import pymysql

pymysql.install_as_MySQLdb()


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
search = Search()
search.init_app(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

@manager.command
def cargar_productos(file):
	import csv

	with open(file) as csvfile:
		lector = csv.DictReader(csvfile)
		for row in lector:
			producto = models.Producto
			producto.id = row['id']
			producto.nombre = row['nombre']
			producto.slug = row['nombre'].replace(' ','-')
			producto.descripcion = row['descripcion']
			producto.peq_desc = row['descripcion'][:150]
			producto.marca_id = row['marca']
			producto.estado = row['estado']
			producto.condicion = row['condicion']
			producto.cant_visto = 0
			db.session.add(producto)

			for i in range(1,7):
				imagen = models.Imagen
				if i == 1:
					imagen.primaria = 1
				else:
					imagen.primaria = 0
				imagen.ruta = row['id'] + '_' + i + '.jpg'
				producto.imagenes.append(imagen)
				db.add(imagen)
		db.session.commit()


