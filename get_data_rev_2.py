import requests
import time


class Node:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        pass

    def try_connect(self):
        """
        Attempts to connect to the node, and will catch error if node cannot be accessed.
        """
        pass

    def to_string(self):
        #return ('%s is at %d' % self.name % self.ip)
        return '%s is at %s' % (self.name, self.ip)

    def update(self):
        """
        Grabs the data being displayed on the site using requests
        """


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
            ip = line[line.find('@') + 1:]
            all_nodes.append(Node(name, ip))
        else:
            pass
    return nodes


def write_csv():
    pass


if __name__ == '__main__':
    nodes = get_node_config('node_config.txt')
    for i in nodes:
        print(i.to_string())