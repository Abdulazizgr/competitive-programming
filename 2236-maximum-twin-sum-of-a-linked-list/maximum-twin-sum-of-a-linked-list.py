# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count = 0
        new_head = ListNode()
        curr_new = new_head 
        prev = None
        max_num = 0
        curr = head
        while curr :
            new_node = ListNode(curr.val)
            curr_new.next = new_node
            curr_new = new_node
            curr = curr.next
    
        curr = head 
        while curr:
            count += 1
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        count = count // 2
        curr = new_head.next
        while count > 0:
            max_num = max(max_num,curr.val + prev.val)
            curr = curr.next
            prev = prev.next
            count  -= 1

        return max_num


     