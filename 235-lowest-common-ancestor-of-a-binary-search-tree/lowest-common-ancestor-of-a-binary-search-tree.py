# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest_common_ancestor (root,p,q):
            if root.val == p.val == q.val:
                return root
            if root.val > p.val and root.val > q.val:
                return lowest_common_ancestor(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return lowest_common_ancestor(root.right,p,q)
            else:
                return root
        
        return lowest_common_ancestor(root,p,q)