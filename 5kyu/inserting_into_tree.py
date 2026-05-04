# Python program to insert element (in level order)
# in Binary Tree
from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to insert element 
# in binary tree
def InsertNode(root, data):
  
    # If the tree is empty, assign new
    # node address to root
    if root is None:
        root = Node(data)
        return root

    # Else, do level order traversal until we find an empty
    # place, i.e. either left child or right child of some
    # node is pointing to NULL.
    q = deque()
    q.append(root)

    while q:
      
        # Fron a front element 
        # in queue
        curr = q.popleft()

        # First check left if left is null 
        # insert node in left otherwise check
        # for right
        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = Node(data)
            return root

        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right = Node(data)
            return root

# Inorder traversal of a binary tree
def inorder(curr):
    if curr is None:
        return
    inorder(curr.left)
    print(curr.data, end=' ')
    inorder(curr.right)

if __name__ == "__main__":
  
    # Constructing the binary tree
    #          10
    #        /    \ 
    #       11     9
    #      /      / \
    #     7      15   8
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)

    key = 12
    root = InsertNode(root, key)

    # After insertion 12 in binary tree
    #          10
    #        /    \ 
    #       11     9
    #      /  \   / \
    #     7   12 15  8
    inorder(root)