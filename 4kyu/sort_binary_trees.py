"""

You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]

"""

from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    
    result = []
    queue = deque([node])  # Use deque for efficient pops from left
    
    while queue:
        current = queue.popleft()  # O(1) operation
        result.append(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return result

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n 


#Other solution



# Example usage:
tree = Node(Node(Node(None, None, 1), Node(None, None, 3), 8), Node(Node(None, None, 4), Node(None, None, 5), 9), 2)
print(tree_by_levels(tree))  # Output: [2, 8, 9, 1, 3, 4, 5]

# Example 1 (matches prompt example 1)
n1 = Node(None, None, 1)
n3 = Node(None, None, 3)
n4 = Node(None, None, 4)
n5 = Node(None, None, 5)
n8 = Node(n1, n3, 8)
n9 = Node(n4, n5, 9)
root1 = Node(n8, n9, 2)