from app import app
from flask import render_template
import time

@app.route('/')
@app.route('/index')
def index():
	user = {'nick':'dimitdim','name':'Dimitar'}
	title = 'test'
	tim = str(time.asctime(time.localtime()))
	return render_template("index.html", title=title, user=user, time=tim)
