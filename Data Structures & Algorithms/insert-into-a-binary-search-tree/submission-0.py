# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        self.insertNode(root, None, val)
        return root
    def insertNode(self, current, prev, val):
        if current == None:
            if prev.val > val:
                prev.left = TreeNode(val)
            else:
                prev.right = TreeNode(val)
        elif val > current.val:
            self.insertNode(current.right, current, val)
        else:
            self.insertNode(current.left, current, val)
            