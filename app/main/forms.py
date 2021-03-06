from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    # q = StringField(_l('Search'), validators=[DataRequired()])
    q = StringField('Buscar...', validators=[DataRequired()])
    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)

class LoginForm(FlaskForm):
	email = StringField('Usuario', validators=[DataRequired()])
	password = PasswordField('Contraseña', validators=[DataRequired()])
	remember_me = BooleanField('Recordarme')
	submit = SubmitField('Iniciar sesion')