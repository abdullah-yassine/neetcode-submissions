# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced_bool = True
        self.balanced(root)
        return self.balanced_bool
    def balanced(self, node): # use postorder
        if node == None:
            return 0
        left_height = self.balanced(node.left)
        right_height = self.balanced(node.right)
        if abs(left_height - right_height) > 1:
            self.balanced_bool = False
            
        return 1 + max(left_height, right_height)