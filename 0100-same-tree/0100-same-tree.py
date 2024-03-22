# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            
            if root1 and root2:
                if root1.val != root2.val:
                    return False
                return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            if root1:
                return False
            if root2:
                return False
            return True
        return dfs(p,q)