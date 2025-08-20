"""
Linked Lists - Insert Nth

Implement a function which inserts a new node at any index within a list.

Given a list, an index n in the range 0..length, and a data element, insert a node in list at index n containing data. Your function should return the head of the list.

//    list            n data
(1 -> 2 -> 3 -> null, 0, 7) ==> 7 -> 1 -> 2 -> 3 -> null
(1 -> 2 -> 3 -> null, 1, 7) ==> 1 -> 7 -> 2 -> 3 -> null
(1 -> 2 -> 3 -> null, 3, 7) ==> 1 -> 2 -> 3 -> 7 -> null
You must throw/raise an exception (specifically ArgumentOutOfRangeException in C#, InvalidArgumentException in PHP) if the index is too large.

The Node class is pre-written for you in the initial code, expect in PHP and Swift where it is preloaded for you in another file.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    # Your code goes here.
    if index<0:
        raise Exception('Index out of range')
    
    new_node = Node(data)

    if index == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(index-1):
        if current is None:
            raise Exception("Index out of range")
        current = current.next
    
    if current is None:
        raise ValueError("Index out of range")
        
    new_node.next = current.next
    current.next = new_node
        
    return head

#Other Solutions
class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt
    
def insert_nth(head, index, data):
  if index == 0: return Node(data, head)
  if head and index > 0:
    head.next = insert_nth(head.next, index - 1, data)
    return head
  raise ValueError