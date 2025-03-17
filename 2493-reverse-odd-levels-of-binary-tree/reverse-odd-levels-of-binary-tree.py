# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        value = deque([root])
        index = 0
        while value:
            ans = []
            for _ in range(len(value)):
                num = value.popleft()
                ans.append(num)
                if num.left:
                    value.append(num.left)
                if num.right:
                    value.append(num.right)
               
            if index % 2 == 1:
                left = 0
                right = len(ans)-1
                while left < right:
                    ans[left].val ,ans[right].val = ans[right].val, ans[left].val 
                    left += 1
                    right -= 1
            index += 1
        return root