""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if not head:
        return Node(data)


    current = head
    if current.data >= data:
        new_elem = Node(data)
        new_elem.next = current
        return new_elem


    while current.next is not None and current.next.data < data:
        current = current.next
    new_elem = Node(data)
    new_elem.next = current.next
    current.next = new_elem
    return head
