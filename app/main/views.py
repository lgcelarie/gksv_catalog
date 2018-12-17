from datetime import datetime
from flask import render_template, session, redirect, url_for, g, request
from . import main
from .forms import SearchForm
from .. import db
from ..models import Producto, Categoria, Visita, Marca


@main.before_app_request
def before_request():
    g.search_form = SearchForm()
    # g.locale = str(get_locale())



@main.route('/', methods=['GET', 'POST'])
def index():
    categorias = Categoria.query.all()
    marcas = Marca.query.all()
    return render_template('index.html', name=session.get('name', False),
        known=session.get('known', False), current_time=datetime.utcnow(),
        categorias=categorias, marcas=marcas)



@main.route('/producto/<slug>')
def producto(slug):
    producto = Producto.query.filter_by(slug=slug).first_or_404()
    import datetime
    visita = Visita(ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        fecha=datetime.datetime.utcnow(),producto_id=producto.id)
    return render_template('product.html', producto=producto)



@main.route('/categoria/<slug>')
def categoria(slug):
    categoria = Categoria.query.filter_by(slug=slug).first_or_404()
    categorias = Categoria.query.all()


    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 20, type=int)
    productos = Producto.query.with_parent(categoria).paginate(page,size,False)
    next_url = url_for('main.categoria', slug=categoria.slug, page=productos.next_num) \
        if productos.has_next else None
    prev_url = url_for('main.categoria', slug=categoria.slug, page=productos.prev_num) \
        if productos.has_prev else None

    return render_template('categoria.html',categoria=categoria, categorias=categorias,
        productos=productos, next_url=next_url, prev_url=prev_url)


@main.route('/marca/<slug>')
def marca(slug):
    marca = Marca.query.filter_by(slug=slug).first_or_404()
    marcas = Marca.query.all()


    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 20, type=int)
    productos = Producto.query.with_parent(marca).paginate(page,size,False)
    next_url = url_for('main.marca', slug=marca.slug, page=productos.next_num) \
        if productos.has_next else None
    prev_url = url_for('main.marca', slug=marca.slug, page=productos.prev_num) \
        if productos.has_prev else None

    return render_template('marca.html',marca=marca, marcas=marcas,
        productos=productos, next_url=next_url, prev_url=prev_url)



@main.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    results = Producto.query.msearch(g.search_form.q.data, fields=['nombre','descripcion']).all()
    # posts, total = Producto.query.msearch(g.search_form.q.data, page,
    #                            20)
    # next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
    #     if total > page * 20 else None
    # prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
    #     if page > 1 else None
    return render_template('search.html', title='Search', productos=results,
                           )

@main.route('/load')
def cargar_productos():
    import csv
    from ..models import Imagen
    file = '/Users/lgcelarie/Documents/flask_cat/gksv_catalog/app/static/cat_pagina.csv'

    with open(file) as csvfile:
        lector = csv.DictReader(csvfile)
        slug_list = list()
        for row in lector:
            print(row)
            producto = Producto()
            producto.id = row['id']
            producto.nombre = row['nombre']
            producto.slug = row['nombre'].replace(' ','-')
            if producto.slug in slug_list:
                producto.slug += str(row['id'])
            slug_list.append(producto.slug)
            producto.descripcion = row['descripcion']
            producto.peq_desc = row['descripcion'][:150]
            producto.marca_id = row['marca']
            producto.estado = row['estado']
            producto.condicion = float(row['condicion'])
            producto.cant_visto = 0
            db.session.add(producto)

            for i in range(1,7):
                imagen = Imagen()
                if i == 1:
                    imagen.primaria = 1
                else:
                    imagen.primaria = 0
                imagen.ruta = row['id'] + '_' + str(i) + '.jpg'
                producto.imagenes.append(imagen)
                db.session.add(imagen)
        db.session.commit()