# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        res = []
        while q:
            level_size = len(q)
            pop = None
            for _ in range(level_size):
                pop = q.popleft()
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            if pop:
                res.append(pop.val)
        return res