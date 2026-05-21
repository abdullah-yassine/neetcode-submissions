# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursionMax(self, currentNode, cnt):
        if currentNode is None:
            return cnt
        left_cnt = self.recursionMax(currentNode.left, cnt + 1)
        right_cnt = self.recursionMax(currentNode.right, cnt + 1)
        return max(left_cnt, right_cnt)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursionMax(root, 0)