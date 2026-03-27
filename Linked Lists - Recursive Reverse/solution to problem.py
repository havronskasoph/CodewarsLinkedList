class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def recursive(current, previous):
        if current is None:
            return previous

        node_next = current.next
        current.next = previous
        return recursive(node_next, current)
    return recursive(head, None)
