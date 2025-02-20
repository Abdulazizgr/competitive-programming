# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(-1)
        right = ListNode(-1)
        curr_left = left
        curr_right = right

        curr = head 
        while curr:
            if curr.val < x:
                new_node= ListNode(curr.val)
                curr_left.next = new_node
                curr_left = new_node
            else:
                new_node= ListNode(curr.val)
                curr_right.next = new_node
                curr_right = new_node
            curr = curr.next
        curr_left.next = right.next

        return left.next

