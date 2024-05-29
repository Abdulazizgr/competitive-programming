# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []

        def fun(root):
            if not root:
                return lis
            lis.append(root.val)
            fun(root.left)
            fun(root.right)
        fun(root)
        return lis