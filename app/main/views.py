from datetime import datetime
from flask import render_template, session, redirect, url_for, g, request
from . import main
from .forms import SearchForm
from .. import db
from ..models import Producto, Categoria, Visita


@main.before_app_request
def before_request():
    g.search_form = SearchForm()
    # g.locale = str(get_locale())



@main.route('/', methods=['GET', 'POST'])
def index():
    categorias = Categoria.query.all()
    return render_template('index.html', name=session.get('name', False),
        known=session.get('known', False), current_time=datetime.utcnow(),
        categorias=categorias)



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




@main.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Producto.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)