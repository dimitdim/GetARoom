"""
Third iteration of the main data collection routine for Kyle and Dimitar's Software Design Project GetARoom
"""

import requests
import time
import os.path
import numpy as np
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed=[]
    def handle_data(self,d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

class Node:
    def __init__(self,name,ip,loc):
        self.name = name
        self.ip   = ip
        self.loc  = loc
		self.file = None
        pass

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
            #print(self.s.get_data())
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
            loc = line[line.find('#')+1:]
            all_nodes.append(Node(name,ip,loc))
        else:
            pass
    return all_nodes

def write_csv_header(nodes):
	"""
	Initialises data files with headers for each active node
	"""
	filename=str(time.strftime("%y%m%d%H%M%S"))+'.csv'
    for node in nodes:
		if not os.path.exists('data/'+node.loc):
			os.makedirs('data/'+node.loc)
		node.file = open('data/'+node.loc+'/'+filename,'w')
		f = node.file
		f.write('Stamp,')
		f.write('Time,')
		for n in node.collect_data():
			f.write(n.partition(':')[0]+',')
		f.write('\n')
    return filename

def write_csv(nodes):
	"""
	Write sensor data to CSV file
	"""
    for node in nodes:
		f = node.file
		f.write(str(time.time)+','+str(time.strftime("%H_%M_%S")))
		for n in node.collect_data():
             f.write(','+str(int(n.partition(':')[2])))
		f.write('\n')
	print '.',

def load_array(filename):
    """
    Loads CSV data into a numpy array
    Don't use this.
    """
    data=np.genfromtext(filename, delimiter=",", autostrip=True, names=True, dtype=int)
    return data

if __name__ == '__main__':
	state1 = True
	while state1:
		nodes = get_node_config('node_config.txt')
		print('Nodes Initialised:')
		for node in nodes:
			print(node.loc)
		filename=write_csv_header(nodes)
		print(filename+' files created')
		state2 = True
		start=time.time()
		try:
			while state2:
				write_csv(nodes)
				state2=os.path.getmtime('node_config.txt')<start
				time.sleep(10)
			print('Config File Modified, restarting')
		except KeyboardInterrupt:
			state1 = False
	f.close()
	print('Data Collection Ended, closing')