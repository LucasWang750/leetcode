# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        if len(nodes) == 1:
            return nodes[0]
        
        def traverse(root):
            if root:
                if root in nodes:
                    return root
                LCA_left = traverse(root.left)
                LCA_right = traverse(root.right)
                if LCA_left and LCA_right:
                    return root
                return LCA_left or LCA_right
        return traverse(root)
                    