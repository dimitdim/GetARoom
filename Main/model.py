__author__ = 'kflores'

"""
Model that defines the class structure of the database.
"""

#Loosely based on all that stuff below this line.  Use those to start.
#Replacing Base with db.model

import random
import requests
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from app import db


Base = declarative_base()


class Node(db.model):
    __tablename__ = "node"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ip = db.Column(db.String)
    loc = db.Column(db.String)
    data = db.relationship('Data',backref = 'author', lazy = 'dynamic')

    def __init__(self, name, ip, loc):
        self.name = name
        self.ip = ip
        self.loc = loc

    def __repr__(self):
        return '%s is at %s in %s' % (self.name, self.ip, self.loc)


class Data(Base):
    __tablename__ = "data"

    id = Column(db.Integer, primary_key=True)
    brightness = Column(db.Integer)
    volume = Column(db,Integer)
    ir = Column(db,Integer)
    temperature = Column(db.Integer)
    node_id = Column(db.Integer, db.ForeignKey("node.id"))

    def __init__(self):
        self.brightness = random.random()
        self.volume = random.random()
        self.ir = random.random()
        self.temperature = random.random()

    def update(self):
        """
        Grabs the data being displayed on the site using requests.  Uses Requests to download HTML, uses HTML Parser to remove tags.
        Returns the page data tagless.
        """
        try:
            self.req = requests.get("http://" + self.ip, timeout=1)
            self.s = MLStripper()
            a = self.req.text[self.req.text.find('<title>'):self.req.text.find('</title>')]
            self.s.feed(self.req.text.replace(a, '\n'))
            self.text = self.s.get_data()

            value_type = ['Brightness', 'Temperature', 'Volume']
            for v in value_type:
                index = self.text.find(v)

        except requests.ConnectionError:
            return '\n'
        except requests.HTTPError:
            return '\n'
        except requests.Timeout:
            return '\n'