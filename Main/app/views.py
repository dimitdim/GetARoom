from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
import time
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN, Node, Data, Status


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
@app.before_request
def before_request():
	g.user = current_user
	g.time = time.asctime()
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
@app.route('/css')
def css():
	return render_template("default.css")


#Pages

@app.route('/')
@app.route('/index')
@login_required
def index():
	title = 'Node List'
	nodes=Node.query.all()
	return render_template("index.html", title=title, user=g.user, time=g.time, nodes=nodes)
@app.route('/node/<id>')
@login_required
def node(id):
	node=Node.query.filter_by(id=id).first()
	title=node.loc
	data=Data.query.filter_by(node_id=id).order_by('localtimestamp desc').first()
	status=Status.query.filter_by(node_id=id).order_by('start desc').first()
	meas=None
	door=None
	if data:
		meas=time.ctime(data.localtimestamp)
		door=time.ctime(data.localtimestamp+(data.last_opened-data.uptime)/1000)
	return render_template("node.html",title=title,user=g.user,time=g.time,data=data,meas=meas,door=door,status=status)

@app.route('/login', methods = ['GET','POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	title = 'Sign In'
	providers = app.config['OPENID_PROVIDERS']
	if form.validate_on_submit():
		flash('OpenID: '+form.openid.data)
		flash('Cookie: '+str(form.remember_me.data))
		session['remember_me']=form.remember_me.data
		return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
	return render_template("login.html", title=title, form=form, user=g.user, time=g.time, providers=providers)
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
