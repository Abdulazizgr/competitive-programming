# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        max_values = []
        value = deque()
        value.append(root)

        while value:
            max_num = -float('inf')
            for idx in range(len(value)):
                num = value.popleft()

                max_num = max(max_num,num.val)
                if num.left:
                    value.append(num.left)
                if num.right:
                    value.append(num.right)
            max_values.append(max_num)
        return max_values

            




        return max_values
