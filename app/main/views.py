from flask import render_template, abort 
from . import main
from flask_login import current_user
from ..models import User 

@main.route('/')
def index():
	return render_template('index.html', current_user=current_user) 

@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user=user)