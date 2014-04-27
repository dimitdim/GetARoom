__author__ = 'kflores'

"""
Model that defines the class structure of the database.
"""

from app import db


class Node(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    uptime = db.Column(db.BigInteger)
    brightness = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    door = db.Column(db.Integer)
    last_opened = db.Column(db.Integer)
    node_id = db.Column(db.Integer, db.ForeignKey("node.id"))

    def __init__(self, uptime, brightness, temperature, volume, door, last_opened):
        self.uptime = uptime
        self.brightness = brightness
        self.temperature = temperature
        self.volume = volume
        self.door = door
        self.last_opened = last_opened

    def __repr__(self):
        return "Light: %s, Temp: %s, Last: %s" % (self.brightness, self.temperature, self.last_opened)
