# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root:Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if root is None:
                return 0
            
            left_size = dfs(root.left)
            right_size = dfs(root.right)

            nonlocal res
            res = max(res,left_size+right_size)

            return max(left_size,right_size)+1

        dfs(root)
        return res
    

if __name__ == "__main__":
    #  Constructed binary tree is
    #          5
    #         / \
    #        1   6
    #       /   / \
    #      3   7   4
    
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
  

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))