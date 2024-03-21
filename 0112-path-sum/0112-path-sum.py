# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(root):
            return root.left is None and root.right is None
        
        def dfs(root, num):
            if root:
                if root.val - num == 0 and isLeaf(root):
                    return True
                return dfs(root.left, num - root.val) or dfs(root.right, num - root.val)
                
        return dfs(root, targetSum)