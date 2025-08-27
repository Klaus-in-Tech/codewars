"""
Linked Lists - Front Back Split

Write a FrontBackSplit() function that takes one list and splits it into two sublists — one for the front half, and one for the back half. If the number of elements is odd, the extra element should go in the front list. For example, FrontBackSplit() on the list 2 -> 3 -> 5 -> 7 -> 11 -> null should yield the two lists 2 -> 3 -> 5 -> null and 7 -> 11 -> null. Getting this right for all the cases is harder than it looks. You will probably need special case code to deal with lists of length < 2 cases.

var source = 1 -> 3 -> 7 -> 8 -> 11 -> 12 -> 14 -> null
var front = new Node()
var back = new Node()
frontBackSplit(source, front, back)
front === 1 -> 3 -> 7 -> 8 -> null
back === 11 -> 12 -> 14 -> null
You should throw an error if any of the arguments to FrontBackSplit are null or if the source list has < 2 nodes.

Hint. Probably the simplest strategy is to compute the length of the list, then use a for loop to hop over the right number of nodes to find the last node of the front half, and then cut the list at that point. There is a trick technique that uses two pointers to traverse the list. A "slow" pointer advances one nodes at a time, while the "fast" pointer goes two nodes at a time. When the fast pointer reaches the end, the slow pointer will be about half way. For either strategy, care is required to split the list at the right point.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def front_back_split(source, front, back):
    if source is None or front is None or back is None:
        raise ValueError("Arguments cannot be null")
    
    if source.next is None:
        raise ValueError("Source list must have at least two nodes")
    
    # Compute the length of the list
    length = 0
    current = source
    while current is not None:
        length += 1
        current = current.next
    
    # Calculate the split index
    split_index = (length + 1) // 2  # For odd, front gets the extra node
    
    # Traverse to the split point
    current = source
    for _ in range(split_index - 1):
        current = current.next
    
    # Split the list
    front.data = source.data
    front.next = source.next
    back.data = current.next.data
    back.next = current.next.next
    current.next = None  # Break the link

    # Test case 1: Even number of nodes
source = Node(2, Node(3, Node(5, Node(7, Node(8)))))
front = Node()
back = Node()
front_back_split(source=source,front=front,back=back)