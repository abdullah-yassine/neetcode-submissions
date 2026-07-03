# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        stack = []
        current = root
        cnt = 0
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            cnt += 1
            if cnt == k:
                return current.val
            current = current.right
        return cnt