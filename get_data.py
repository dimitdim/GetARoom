import urllib2
from bs4 import BeautifulSoup
import time

def update(ip):
    req = urllib2.Request(ip)
    try: f=urllib2.urlopen(req)
    except URLError, e:
        print e.reason
    soup=BeautifulSoup(f)
    title=soup.title.string
    alltext=(soup.get_text())
    return alltext.replace(title,'')

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
    
if __name__ == '__main__':
    node_ips=["http://10.26.66.19","http://10.26.66.29"]
    elapsed=0
    while True:
        for m in range(len(node_ips)):
            print(parse_data(update(node_ips[m])))
        time.sleep(1)
        elapsed+=1
        print(elapsed)