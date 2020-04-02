from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from models import User
from flask import request


class LoginForm(FlaskForm):
    username = StringField('Nome utente', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Mantieni accesso')
    submit = SubmitField('Accedi')
