# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) -1

        def binarySearchTree (left,right):
            if left > right :
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left =binarySearchTree(left,mid-1)
            node.right= binarySearchTree(mid+1,right)

            return node
        return binarySearchTree(left,right)



