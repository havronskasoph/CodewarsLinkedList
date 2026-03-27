class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pairs(head):
    if not head or not head.next:
        return head

    right = head
    left = head.next
    right.next = swap_pairs(left.next)
    left.next = right

    return left
