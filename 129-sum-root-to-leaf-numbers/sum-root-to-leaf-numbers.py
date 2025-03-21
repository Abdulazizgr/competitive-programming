# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def findPath(root, prev, ans):
            if root is None:
                return
            
            prev += str(root.val)  
            if root.left is None and root.right is None:  
                ans[0] += int(prev)  
                return 
            
            findPath(root.left, prev, ans)  
            findPath(root.right, prev, ans)  
        
        ans = [0]  
        findPath(root, "", ans)
        return ans[0]


        # def findPath (root,path,value):
        #     if root is None:
        #         return 0
        #     path.append(str(root.val))
        #     if root.left is None and root.right is None:
        #         num = int("".join(path))
        #         path.pop()
        
        #         return num
            
        #     left  = findPath(root.left,path,value)
        #     right = findPath (root.right,path,value)
        #     path.pop()
        #     return left + right 
        # path = []
        # value = root.val
        # return findPath(root,path,value)
