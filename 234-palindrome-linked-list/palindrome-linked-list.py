# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_ls = ListNode(-1)
        curr = new_ls
        new_head = head
        while new_head:
            new_node = ListNode(new_head.val)
            curr.next = new_node
            curr = new_node
            new_head = new_head.next
        prev = None
        curr = new_ls.next

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        while head and prev:
            
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

