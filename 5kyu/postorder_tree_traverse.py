class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def postorder(node,res):
    if node is None:
        return
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    res = []
    postorder(root,res)
    for node in res:
        print(node,end=" ")
        
        