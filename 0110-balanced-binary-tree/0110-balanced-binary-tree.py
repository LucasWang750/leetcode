# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return -1
            return 1 + max(height(root.left), height(root.right))
        
        def dfs(root):
            if root:
                height_left = height(root.left)
                height_right = height(root.right)
                return abs(height_left - height_right) < 2 and dfs(root.left) and dfs(root.right)
            else:
                return True
        return dfs(root)