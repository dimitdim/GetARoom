from app import app
from flask import render_template, flash, redirect
import time
from forms import LoginForm


user = {'nick':'dimitdim','name':'Dimitar'}
tim = str(time.asctime(time.localtime()))

@app.route('/')
@app.route('/index')
def index():
	title = 'test'
	return render_template("index.html", title=title, user=user, time=tim)

@app.route('/login', methods = ['GET','POST'])
def login():
	form = LoginForm()
	title = 'Sign In'
	if form.validate_on_submit():
		flash('OpenID: '+form.openid.data+'\nremember_me: '+str(form.remember_me.data))
		return redirect('/index')
	return render_template("login.html", title=title, form=form, user=user, time=tim)

@app.route('/css')
def css():
	return render_template("default.css")
