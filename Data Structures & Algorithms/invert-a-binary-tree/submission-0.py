# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertRecursion(self, currentNode):
        if currentNode is None:
            return
        self.invertRecursion(currentNode.left)
        self.invertRecursion(currentNode.right)
        temp = currentNode.left
        currentNode.left = currentNode.right
        currentNode.right = temp
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertRecursion(root)
        return root