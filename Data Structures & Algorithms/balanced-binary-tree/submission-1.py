# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, root) -> int:  
        if root == None: 
            return 0 
        return 1+ max(self.checkHeight(root.left), self.checkHeight(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        x = self.checkHeight(root.left)
        y = self.checkHeight(root.right)
         
        if (x - y) < -1 or (x-y) > 1: 
            return False
    
        x = self.isBalanced(root.left)
        y = self.isBalanced(root.right) 

        if not x or not y:
            return False

        return True 
        

        
        
                