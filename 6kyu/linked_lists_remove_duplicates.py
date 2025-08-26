"""
Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if not head:
        return None
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


#Other Solutions
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    dum = head
    while head:
        while head.next and head.data == head.next.data:
            head.next = head.next.next
        head = head.next
    return dum