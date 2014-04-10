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
    f = open('data'+str(time.strftime("%y%m%d%H%M%S"))+'.csv','w')
    node_ips=["http://10.26.66.39"]
    names=["Kyle","Dimitar"]
    f.write('Time')
    for m in range(len(node_ips)):
        for n in parse_data(update(node_ips[m])):
            f.write(','+str(names[m])+'_'+n.partition(':')[0])
    f.write('\n')
    while True:
        f.write(str(time.strftime("%H_%M_%S")))
        for m in node_ips:
            for n in parse_data(update(m)):
                f.write(','+n.partition(':')[2])
        f.write('\n')
        time.sleep(1)
    f.close()
