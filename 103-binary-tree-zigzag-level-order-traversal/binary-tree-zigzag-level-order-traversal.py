# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        value = deque([root])
        left = True
        while value:
            res = []
            for _ in range(len(value)):
                if left:
                    num = value.popleft()
                    if num.left:
                        value.append(num.left)
                    if num.right:
                        value.append(num.right) 
                else:
                    num = value.pop()
                    if num.right:
                        value.appendleft(num.right) 
                    if num.left:
                        value.appendleft(num.left)
                res.append(num.val)
            left = not left
            ans.append(res)
        return ans