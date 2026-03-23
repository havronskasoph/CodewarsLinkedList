from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    new_elem = Node(data)
    new_elem.next = head
    return new_elem

def build_one_two_three():
    build_from_scratch = None
    build_from_scratch = push(build_from_scratch, 3)
    build_from_scratch = push(build_from_scratch, 2)
    build_from_scratch = push(build_from_scratch, 1)
    return build_from_scratch
