from app import db, models
import requests
import ast
import time


def update(ip):
    """
    Grabs the data being displayed on the site using requests.
    Returns the page data as a dictionary, but the page better be formatted to look like a dictionary.. Btw, ip is a string.
    Example string on page: {'uptime': '00:00:02','brightness':156,'temperature':23,'volume':491}
    """
    try:
        req = requests.get("http://" + ip, timeout=5)
        out_dict = ast.literal_eval(req.text[req.text.find('{'):req.text.find('}')+1])
        return out_dict
    except requests.ConnectionError:
        return 'error'
    except requests.HTTPError:
        return 'error'
    except requests.Timeout:
        return 'error'


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
            all_nodes.append(models.Node(name, ip, loc))
        else:
            pass
    return all_nodes


def check_node_exist(node_object):
    """
    Checks a node location and checks if that node already exists in the database.  Returns true or false.
    """
    nodes = models.Node.query.all()
    for n in nodes:
        if n.loc == node_object.loc:
            return True
    return False


def update_database():
    for n in get_node_config('node_config.txt'):
        if not check_node_exist(n):  #Basically, if the node does not already exist, create it now.
            db.session.add(n)
            print(n)
    for k in models.Node.query.all():
        d = update(k.ip)
        if len(d) == 4:
            data = models.Data(time.time(),d['uptime'], d['brightness'], d['temperature'], d['volume'], 0, 0, k)
        else:
            data = models.Data(0, 0, 0, 0, 0, 0, 0, k)
        db.session.add(data)
    db.session.commit()

if __name__ == '__main__':
    update_database()
