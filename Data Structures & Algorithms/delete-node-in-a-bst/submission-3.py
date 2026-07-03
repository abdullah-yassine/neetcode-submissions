# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == key:
            if root.left == None or root.right == None:
                return root.left if root.left else root.right
            else:
                print("hello")
                succ = root.right
                while succ.left:
                    succ = succ.left
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
                return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        else:
            root.right = self.deleteNode(root.right,key)
        return root
            
