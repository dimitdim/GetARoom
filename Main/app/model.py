__author__ = 'kflores'

"""
Model that defines the class structure of the database.
"""


import random
from app import db


class Node(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ip = db.Column(db.String)
    loc = db.Column(db.String)
    data = db.relationship('Data', backref='author', lazy='dynamic')

    def __init__(self, name, ip, loc):
        self.name = name
        self.ip = ip
        self.loc = loc

    def __repr__(self):
        return '%s is at %s in %s' % (self.name, self.ip, self.loc)


class Data(db.model):
    id = db.Column(db.Integer, primary_key=True)
    brightness = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    ir = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    node_id = db.Column(db.Integer, db.ForeignKey("node.id"))

    def __init__(self):
        self.brightness = random.random()
        self.volume = random.random()
        self.ir = random.random()
        self.temperature = random.random()

    def __repr__(self):
        return "Just a data object :)"
