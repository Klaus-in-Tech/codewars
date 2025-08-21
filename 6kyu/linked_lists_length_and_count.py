"""
Linked Lists - Length & Count

Implement length to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
"""

from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

def length(node: Node) -> int:
    curr_node = node
    counter = 0
    while curr_node is not None:
        counter+=1
        curr_node = curr_node.next                    
    return counter
  
def count(node: Node, data) -> int:
    current = node
    count_value =0
    while current is not None:
        if current.data == data:
            count_value +=1
        current = current.next
    return count_value

#Other Solutions
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def length(node):
  if node:
    return 1 + length(node.next)
  return 0
  
def count(node, data):
  if node:
    if node.data == data:
      return 1 + count(node.next, data)
    return count(node.next, data)
  return 0