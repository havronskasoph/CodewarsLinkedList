def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    the_length_of_loop = 1
    fast = fast.next

    while fast != slow:
        fast = fast.next
        the_length_of_loop += 1
    return the_length_of_loop
