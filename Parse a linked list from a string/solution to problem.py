from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    list_splited = list_repr.split(" -> ")
    if list_splited[0] == 'None':
        return None

    head = Node(int(list_splited[0]))
    current = head
    for elem in range( 1, len(list_splited) - 1):
        the_value = int(list_splited[elem])
        data_ = Node(the_value)
        current.next = data_
        current = current.next
    return head
