__author__ = 'kflores'

"""
Model that defines the class structure of the database.
"""

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Node(db.Model):
    """class representation of one networked sensor kit hooked into ethernet.  Instatiation requires the name, ip address, and location of the "node", but all of these values should be placed into the config file (see get_node_config(filename) in download_data.py)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ip = db.Column(db.String)
    loc = db.Column(db.String, index=True, unique=True)
    data = db.relationship('Data', backref='origin', lazy='dynamic')

    def __init__(self, name, ip, loc):
        self.name = name
        self.ip = ip
        self.loc = loc

    def __repr__(self):
        return '%s is at %s in %s' % (self.name, self.ip, self.loc)


class Data(db.Model):
    """
    Class representation of one data row in the datatable.  This object records the local time, node uptime, brightness, temperature, door IR sensor, and the time the door was last opened.  Volume is a dummy variable for feature that is not yet implemented.  node_id ties the Data objects to the node object that created them (the location they are at)
    """
    id = db.Column(db.Integer, primary_key=True)
    localtimestamp = db.Column(db.Integer)
    uptime = db.Column(db.Integer)
    brightness = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    door = db.Column(db.Integer)
    last_opened = db.Column(db.Integer)
    node_id = db.Column(db.Integer, db.ForeignKey("node.id"))

    def __init__(self, localtimestamp, uptime, brightness, temperature, volume, door, last_opened, origin):
        self.localtimestamp = localtimestamp
        self.uptime = uptime
        self.brightness = brightness
        self.temperature = temperature
        self.volume = volume
        self.door = door
        self.last_opened = last_opened
        self.origin = origin

    def __repr__(self):
        return "Light: %s, Temp: %s, Last: %s" % (self.brightness, self.temperature, self.last_opened)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Status(db.Model):
    """
    Object for storing room status values.  An analysis routine that processes sensor data and reaches a conclusion on room state will instatiate these objects.  WIP.
    """
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    node_id = db.Column(db.Integer, db.ForeignKey("node.id"))

    def __init__(self, start, status, origin):
        self.start = start
        self.status = status
        self.origin = origin
