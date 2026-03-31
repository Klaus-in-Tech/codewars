"""
Remove Dups (Unsorted Linked List)

Write code to remove duplicates from an unsorted linked list.
The first occurrence of each value should be kept.
"""

try:
    from preloaded import Node
except Exception:
    class Node(object):
        def __init__(self, data, nxt=None):
            self.data = data
            self.next = nxt


def remove_dups(head):
    """Remove duplicate values from an unsorted singly linked list in-place.

    Keeps the first occurrence of each value and removes later duplicates.
    Returns the head of the modified list.
    """
    if head is None:
        return None

    seen = {head.data}
    prev = head
    current = head.next

    while current is not None:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next

    return head

# Test cases
def print_list(node):
    values = []
    while node is not None:
        values.append(node.data)
        node = node.next
    return values   

# Example 1
head1 = Node(1, Node(2, Node(3, Node(2, Node(4)))))
new_head1 = remove_dups(head1)
print(print_list(new_head1))  # Output: [1, 2, 3, 4]