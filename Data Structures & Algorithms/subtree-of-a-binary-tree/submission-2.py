# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: #preorder
        if root == None:
            return False
        if self.isEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
            
    def isEqual(self, p, q): # preorder
        if p == q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)
