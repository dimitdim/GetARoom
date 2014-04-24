"""
Third iteration of the main data collection routine for Kyle and Dimitar's Software Design Project GetARoom
"""

import requests
import time
import os.path
import random

from HTMLParser import HTMLParser

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


class Node(Base):
    __tablename__ = "node"
    # id = Column(Integer, primary_key=True)
    name = Column(String,primary_key=True)

    def __init__(self, name, ip, loc):
        self.name = name
        self.ip = ip
        self.loc = loc


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    brightness = Column(Integer)
    volume = Column(Integer)
    ir = Column(Integer)
    temperature = Column(Integer)

    node_name = Column(Integer, ForeignKey("node.name"))
    node = relationship("Node", backref=backref("data", order_by=id))

    def __init__(self):
        self.brightness = random.random()
        self.volume = random.random()
        self.ir = random.random()
        self.temperature = random.random()

    def to_string(self):
        #Prints the name, ip, and  physical location.
        return '%s is at %s in %s' % (self.name, self.ip, self.loc)

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


def get_node_config(location):
    """
    Reads the config file at the specified location, uses the config file to identify nodes.
    Constructs Node objects based on the data in the config file.
    """
    all_nodes = []
    text = open(location, 'r')
    for line in text:
        if line[0] != '\n' and '@' in line:
            name = line[0:line.find('@') - 1]
            ip = line[line.find('@') + 1:line.find('#') - 1]
            loc = line[line.find('#') + 1:line.find('\n')]
            all_nodes.append(Node(name, ip, loc))
        else:
            pass
    return all_nodes


if __name__ == '__main__':
    engine = create_engine('sqlite:///SensorData.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    nodes = get_node_config('node_config.txt')  #Load nodes from configuration file
    while True:
        try:
            for n in nodes:
                n.data = [Data()]  #The plan is for the __init__ method of data to call the update function and assign the values to one data object.
                session.add(n)
            session.commit()
            time.sleep(1)
        except KeyboardInterrupt:
            print('Canceled by user.')
