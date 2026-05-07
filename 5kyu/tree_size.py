class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        
def get_size_of_the_tree(root):
    if root is None:
        return 0
        
    left_size = get_size_of_the_tree(root.left)
    right_size = get_size_of_the_tree(root.right)
    
    return left_size+right_size+1

if __name__ == "__main__":

    #  Constructed binary tree is
    #          5
    #         / \
    #        1   6
    #       /   / \
    #      3   7   4
    
    root = Node(5)
    root.left = Node(1)
    root.right = Node(6)

    root.left.left = Node(3)

    root.right.left = Node(7)
    root.right.right = Node(4)

    print(get_size_of_the_tree(root))