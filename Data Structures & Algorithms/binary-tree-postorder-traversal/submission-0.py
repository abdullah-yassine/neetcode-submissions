# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result =[]
        self.postorder(root, result)
        return result
    def postorder(self, node, result):
        if node == None:
            return 
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)
