# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(root):
            return not root.left and not root.right 
        
        def dfs(root, num):
            if not root:
                return False
            num -= root.val
            if isLeaf(root):
                return num == 0
            return dfs(root.left, num) or dfs(root.right, num)
        return dfs(root, targetSum)