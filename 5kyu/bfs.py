class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
        
def level_order(root):
    if not root:
        return []
        
    res,q,curr_level = [],[],0
    q.append(root)
    while q:
        lenq = len(q)
        res.append([])
        for _ in range(lenq):
            node = q.pop(0)
            res[curr_level].append(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        curr_level+=1
        
    return res
    
        
if __name__ == "__main__":
    
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)
    
    res = level_order(root)
     
    for level in res:
        for val in level:
            print(val,end=" ")
        print()