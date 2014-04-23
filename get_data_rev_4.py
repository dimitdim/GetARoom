"""
Third iteration of the main data collection routine for Kyle and Dimitar's Software Design Project GetARoom
"""

import requests
import time
import os.path
from HTMLParser import HTMLParser

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed=[]
    def handle_data(self,d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

class Node(Base):
    __tablename__="Nodes"
    time=Column(Integer, primary_key=True)
    name=Column(String)
    brightness=Column(Integer)
    sound=Column(Integer)
    ir=Column(Integer)
    temperature=Column(Integer)

    def __init__(self,name,ip,loc):
        self.name = name
        self.ip   = ip
        self.loc  = loc
        self.brightness=0
        self.sound=0
        self.ir=0
        self.temperature=0

    def to_string(self):
        #Prints the name, ip, and  physical location.
        return '%s is at %s in %s' % (self.name, self.ip, self.loc)

    def update(self):
        """
        Grabs the data being displayed on the site using requests.  Uses Requests to download HTML, uses HTML Parser to remove tags.
        Returns the page data tagless.
        """
        try:
            self.req=requests.get("http://"+self.ip,timeout=1)
            self.s=MLStripper()
            a=self.req.text[self.req.text.find('<title>'):self.req.text.find('</title>')]
            self.s.feed(self.req.text.replace(a,'\n'))
            return self.s.get_data()
        except requests.ConnectionError:
            return '\n'
        except requests.HTTPError:
            return '\n'
        except requests.Timeout:
            return '\n'
        
    def parse_data(self,text):
        """
        Takes in the plain text resulting from update.
        Returns the data as a dictionary in sensor:value
        """
        indices=[] #Empty list to find all instances of \n
        data=[]
        for i in range(len(text)):
            if text[i] == '\n':
                indices.append(i)
        for k in range(len(indices)):
            data.append(str(text[indices[k-1]+1:indices[k]]))
        return data[1:]
        
    def collect_data(self):
        """
        Basically calls update and parse in rapid succession.  The two functions were kept separate incase the unparsed data 
        is ever desired.
        """
        return self.parse_data(self.update())

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
            ip = line[line.find('@') + 1:line.find('#')-1]
            loc = line[line.find('#')+1:line.find('\n')]
            all_nodes.append(Node(name,ip,loc))
        else:
            pass
    return all_nodes


if __name__ == '__main__':
    engine = create_engine('sqlite:///SensorData.db',echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session=Session()
    node1=Node('dummy','0,0,0','here')
    session.add(node1)
    session.commit()
    
    
    # state1 = True
    # while state1:
        # nodes = get_node_config('node_config.txt')
        # print('Nodes Initialised:')
        # for node in nodes:
            # print(node.loc)
        # filename=write_csv_header(nodes)
        # print(filename+' files created')
        # state2 = True
        # start=time.time()
        # try:
            # while state2:
                # write_csv(nodes)
                # state2=os.path.getmtime('node_config.txt')<start
                # time.sleep(10)
            # print('Config File Modified, restarting')
        # except KeyboardInterrupt:
            # state1 = False
    # for node in nodes:
        # node.file.close()
    # print('Data Collection Ended, closing')
