def stringify(node):
    output = ""
    current = node
    while current is not None:
        output += str(current.data)
        output += " -> "
        current = current.next
    output += "None"
    return output
