"""
Second iteration of  the main data collection routine for Kyle and Dimitar's Software Design Project
"""


import requests
import time
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
    def __init__(self, name, ip,loc):
        self.name = name
        self.ip = ip
        self.loc=loc
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
            self.req=requests.get("http://"+self.ip,timeout=0.01)
            self.s=MLStripper()
            a=self.req.text[self.req.text.find('<title>'):self.req.text.find('</title>')]
            self.s.feed(self.req.text.replace(a,'\n'))
            return self.s.get_data()
        except requests.ConnectionError:
            return '\n 0,'
        except requests.HTTPError:
            return '\n 0,'
        except requests.Timeout:
            return '\n 0,'
        

def parse_data(text):
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
            all_nodes.append(Node(name, ip,loc))
        else:
            pass
    return all_nodes


def write_csv(nodes):
    f = open('data'+'_'+str(time.strftime("%y%m%d%H%M%S"))+'.csv','w')
    f.write('Time,')
    for m in nodes:
        for n in parse_data(m.update()): #As it turns out, only nodes connected when this script runs are loaded into CSV.
            f.write(m.name+'_'+n.partition(':')[0]+',')
    f.write('\n')
    try:
        while True:
            f.write(str(time.strftime("%H_%M_%S")))
            for m in nodes:
                for n in parse_data(m.update()):
                     f.write(','+n.partition(':')[2])
            f.write('\n')
            time.sleep(1)
            print '.',
    except KeyboardInterrupt:
        print('Data Collection Ended.')
    f.close()
    print('File Closed.')

if __name__ == '__main__':
    nodes = get_node_config('node_config.txt')
    write_csv(nodes)