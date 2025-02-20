# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        idx = 0
        curr = head
        while curr:
            if curr in dic:
                return curr
            dic[curr] = idx
            idx += 1
            curr = curr.next
       


       