"""
Linked Lists - Get Nth
Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on.

So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
The index should be in the range [0..length-1]. If it is not, or if the list is empty, GetNth() should throw/raise an exception (ArgumentException in C#, InvalidArgumentException in PHP, Exception in Java).
"""

from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    # Your code goes here.
    # Traverse through the linked list
    if not node:
        raise Exception("Empty LinkedList")
    if index < 0:
        raise Exception("Index cannot be negative")
    curr_node = node
    while index > 0:
        if curr_node.next is None:
            raise Exception("Index out of bounds")
        curr_node = curr_node.next
        index-=1
    return curr_node
    #Return a value whose index is equal to the given index


#Other Solutions
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    v = -1
    n = node
    while n:
        v += 1
        if v == index:
        	return n
        n = n.next
    
    raise ValueError
