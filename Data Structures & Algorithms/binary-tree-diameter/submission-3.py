# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = {"value" : 0}
        self.diameter(root, result)
        return result["value"]
    def diameter(self, node, result): # use postorder so we can add left + right
        if node == None:
            return 0
        left_height = self.diameter(node.left, result)
        right_height = self.diameter(node.right, result)
        result["value"] = max(result["value"], left_height + right_height)
        return 1 + max(left_height, right_height)
