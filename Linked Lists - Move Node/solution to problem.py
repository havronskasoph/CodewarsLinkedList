class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError
    first = source
    source = source.next
    first.next = dest
    dest = first
    return Context(source, dest)
