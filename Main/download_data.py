from app import db, models
import requests
import ast
import time
import os.path


def update(ip):
    """
    Grabs the data being displayed on the site using requests.
    Returns the page data as a dictionary, but the page better be formatted to look like a dictionary.. Btw, ip is a string.
    Example string on page: {'uptime': '00:00:02','brightness':156,'temperature':23,'volume':491}
    """
    try:
        req = requests.get("http://" + ip, timeout=5)
        out_dict = ast.literal_eval(req.text[req.text.find('{'):req.text.find('}') + 1])
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


def check_node_exist(new_nodes):
    """
    Checks a node location and checks if that node already exists in the database.  Returns true or false.
    """
    all_nodes = models.Node.query.all()
    all_node_loc=[]
    for node in all_nodes:
        all_node_loc.append(node.loc)
    for n in range(len(new_nodes)):
	node=new_nodes[n]
        if node.loc in all_node_loc:
	    node_old=models.Node.query.filter_by(loc=node.loc).first()
	    node_old.name=node.name
	    node_old.ip=node.ip
            new_nodes[n]=node_old
	else:
            db.session.add(node)
    db.session.commit()

def update_database(nodes):
    for node in nodes:
        d = update(node.ip)
        d_field = {'uptime': -1, 'brightness': -1, 'temperature': -1, 'volume': -1, 'door': -1, 'last': -1}
        if type(d) == dict:
            for key in d_field:
                if key in d:
                    d_field[key] = d[key]
        data = models.Data(time.time(), d_field['uptime'], d_field['brightness'], d_field['temperature'], d_field['volume'], d_field['door'], d_field['last'], node) #All the values being passed into data are going to be integers
        db.session.add(data)
    db.session.commit()
    print '.',


if __name__ == '__main__':
    state1 = True
    while state1:
        nodes = get_node_config('node_config.txt')
        check_node_exist(nodes)  #Basically, if the node does not already exist, create it now.
        print('Nodes Initialised:')
	for node in nodes: print(node.id)
        state2 = True
        start=time.time()
        try:
            while state2:
                update_database(nodes)
                state2=os.path.getmtime('node_config.txt')<start
                time.sleep(10)
            print('Config File Modified, restarting')
        except KeyboardInterrupt:
            state1 = False
    print('Data Collection Ended, closing')
