from datetime import datetime
from flask import render_template, session, redirect, url_for, g
from . import main
from .forms import SearchForm
from .. import db
from ..models import Producto


@main.before_app_request
def before_request():
    g.search_form = SearchForm()
    # g.locale = str(get_locale())



@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name=session.get('name'),
        known=session.get('known', False), current_time=datetime.utcnow())



@main.route('/producto/<slug>')
def producto(slug):
    producto = Producto.query.filter_by(slug=slug).first()
    if producto is None:
        abort(404)
    stars = (int(producto.condicion)/2,round(producto.condicion%2))
    return render_template('product.html', producto=producto, stars = stars)



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