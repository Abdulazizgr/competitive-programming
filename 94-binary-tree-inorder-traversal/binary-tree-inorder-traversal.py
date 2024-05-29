# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []

        def fun(root):
            if not root:
                return lis
            
            fun(root.left)
            lis.append(root.val)
            fun(root.right)
        fun(root)
        return lis