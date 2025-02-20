# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_ls = ListNode(-1)
        new_head = head
        curr = new_ls

        while new_head:
            if new_head.val != val:
                new_node = ListNode(new_head.val)
                curr.next = new_node
                curr = new_node
            new_head = new_head.next
        return new_ls.next

