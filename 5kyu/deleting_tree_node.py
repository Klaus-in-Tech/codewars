# Python program to delete a specific 
# element in a binary tree

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to delete the deepest node
# in the binary tree
def delete_deepest(root, dNode):
    queue = [root]

    while queue:
        curr = queue.pop(0)

        # If current node is the deepest 
        # node, delete it
        if curr == dNode:
            curr = None
            del dNode
            return

        # Check the right child first
        if curr.right:
          
            # If right child is the deepest
            # node, delete it
            if curr.right == dNode:
                curr.right = None
                del dNode
                return
            queue.append(curr.right)

        # Check the left child
        if curr.left:
          
            # If left child is the deepest
            # node, delete it
            if curr.left == dNode:
                curr.left = None
                del dNode
                return
            queue.append(curr.left)

# Function to delete the node with the given key
def deletion(root, key):

    if root is None:
        return None

    # If the tree has only one node
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root

    queue = [root]
    curr = None
    keyNode = None

    # Level order traversal to find the
    # deepest node and the key node
    while queue:
        curr = queue.pop(0)

        # If current node is the key node
        if curr.data == key:
            keyNode = curr

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    # If key node is found, replace its
    # data with the deepest node
    if keyNode is not None:
      
        x = curr.data
        
        # Replace key node data with 
        # deepest node's data
        keyNode.data = x
        
        # Delete the deepest node
        delete_deepest(root, curr)

    return root

# Inorder traversal of a binary tree
def inorder(curr):
    if curr is None:
        return
    inorder(curr.left)
    print(curr.data, end=" ")
    inorder(curr.right)

if __name__ == "__main__":
  
    # Construct the binary tree
    #       10         
    #      /  \       
    #    11    9
    #   / \   / \     
    #  7  12 15  8     

    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right.left = Node(15)
    root.right.right = Node(8)

    key = 11
    root = deletion(root, key) 

    inorder(root)