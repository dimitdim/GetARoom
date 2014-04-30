from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
import time
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN


user = {'nick': 'dimitdim', 'name': 'Dimitar'}
tim = str(time.asctime(time.localtime()))


@app.route('/')
@app.route('/index')
def index():
    title = 'test'
    return render_template("index.html", title=title, user=user, time=tim)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    title = 'Sign In'
    providers = app.config['OPENID_PROVIDERS']
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    if form.validate_on_submit():
        flash('OpenID: ' + form.openid.data)
        flash('Cookie: ' + str(form.remember_me.data))
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template("login.html", title=title, form=form, user=user, time=tim, providers=providers)


@app.route('/css')
def css():
    return render_template("default.css")


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))
