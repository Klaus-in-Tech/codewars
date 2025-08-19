"""
Linked Lists - Push & BuildOneTwoThree

Write push() and buildOneTwoThree() functions to easily update and initialize linked lists. Try to use the push() function within your buildOneTwoThree() function.

Here's an example of push() usage:

var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null
The push function accepts head and data parameters, where head is either a node object or null/None/nil. Your push implementation should be able to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes: 1 -> 2 -> 3 -> null
"""


from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    # Your code goes here.
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def build_one_two_three():
    # Your code goes here.
    head = None
    head = push(head,3)
    head = push(head,2)
    head = push(head,1)
    return head


#Other Solutions
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    return Node(1, Node(2, Node(3)))