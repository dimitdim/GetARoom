import urllib2
from bs4 import BeautifulSoup
import time

def update():
    req = urllib2.Request("http://10.26.66.19")
    try: f=urllib2.urlopen(req)
    except URLError, e:
        print e.reason
    soup=BeautifulSoup(f)
    title=soup.title.string
    alltext=(soup.get_text())
    return alltext.replace(title,'')

if __name__ == '__main__':
    elapsed=0
    while True:
        print(update())
        time.sleep(1)
        elapsed+=1
        print(elapsed)