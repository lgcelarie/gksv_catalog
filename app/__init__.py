from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login = LoginManager()
from .admin_views import DashboardView
admin = Admin(name='Geekingdom SV Admin', template_mode='bootstrap3', index_view=DashboardView())
# Add administrative views here

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login.init_app(app)
    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'slate'
    admin.init_app(app)
    from . import models
    admin.add_view(ModelView(models.Producto, db.session))
    admin.add_view(ModelView(models.Marca, db.session))
    admin.add_view(ModelView(models.Categoria, db.session))    
    #admin.add_view(DashboardView(name='Dashboard')) 
    # attach routes and custom error pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

