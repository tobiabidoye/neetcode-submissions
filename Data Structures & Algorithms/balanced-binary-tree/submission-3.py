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
        
        x = 1 + self.height(root.left)
        y = 1 + self.height(root.right)

        return max(x,y)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None: 
            return True
        
        if abs(self.height(root.right) - self.height(root.left)) > 1:
            return False
        
        x = self.isBalanced(root.left)
        y =self.isBalanced(root.right)
     
        if not x or not y: 
            return False

        return True 
            
        


