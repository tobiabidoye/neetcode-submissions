# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def height(self, root) -> int: 
        if root == None: 
            return 0
        
        x = self.height(root.left)
        y = self.height(root.right)

        if x == -1 or y == -1: 
            return -1
    
        if abs(x - y) > 1: 
            return -1
        return 1 + max(x,y)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if self.height(root) == -1: 
            return False

        return True        
