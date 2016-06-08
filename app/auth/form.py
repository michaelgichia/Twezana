from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class LoginForm(Form):
	email = StringField('Email:', validators=[Required(), Email()])
	password = PasswordField('Password:', validators=[Required()])
	remember_me = BooleanField('Keep me logged in!', default=False)
	submit = SubmitField('Login')