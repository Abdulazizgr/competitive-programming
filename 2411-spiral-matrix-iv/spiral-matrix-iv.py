# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top , left = 0,0 
        bottom = m -1
        right = n -1

        ans = [[-1 for _ in range(n)] for _ in range(m)]
 
        while bottom >= top and right >= left:
            # to the right 
            for col in range(left, right + 1):
                if head:
                    ans[top][col] = head.val
                    head = head.next
            top += 1 
            if left <= right:
                # to the bottom
                for row in range(top,bottom + 1):
                    if head:
                        ans[row][right] = head.val
                        head = head.next
                right -= 1
            
            if top <= bottom:
                # to the left
                for col in range(right,left-1,-1):
                    if head:
                        ans[bottom][col] = head.val
                        head = head.next
                bottom -= 1

            if left <= right:
                # to the top
                for row in range(bottom,top-1,-1):
                    if head:
                        ans[row][left] = head.val
                        head = head.next
                        
                left += 1    

        return ans