# from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node == None:
        raise ValueError

    the_length = 0
    cur_len = node
    while cur_len is not None:
        cur_len = cur_len.next
        the_length += 1

    if index >= the_length or index < 0:
        raise ValueError


    count = 0
    current = node
    while count != index:
        current = current.next
        count += 1
    return current
