class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    the_head1 = head
    the_head2 = head.next
    current1 = the_head1
    current2 = the_head2
    while current1 and current2:
        current1.next = current2.next
        current1 = current1.next

        if current1:
            current2.next = current1.next
            current2 = current2.next
    return Context(the_head1, the_head2)
