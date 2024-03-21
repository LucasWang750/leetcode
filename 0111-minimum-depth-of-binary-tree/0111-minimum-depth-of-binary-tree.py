# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(root):
            return root.left is None and root.right is None
        
        def dfs(root, height):
            if root is None:
                return 0
            if isLeaf(root):
                return height
            else:
                if root.left is None:
                    return dfs(root.right, height + 1)
                elif root.right is None:
                    return dfs(root.left, height + 1)
                return min(dfs(root.left, height + 1), dfs(root.right, height + 1))
        return dfs(root, 1)