# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        curr_l1 = l1
        curr_l2 = l2
        curr = new_head
        flag = 0

        while curr_l1 and curr_l2:
            _sum = curr_l1.val + curr_l2.val
            _sum += flag
            if _sum > 9:
                new_node = ListNode(int(str(_sum)[-1]))
                curr.next = new_node
                curr = new_node
                flag = 1
            else:
                new_node = ListNode(_sum)
                curr.next = new_node
                curr = new_node
                flag = 0

            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
        if _sum > 9:
                new_node = ListNode(1)
                curr.next = new_node
        if curr_l1:
            while curr_l1 :
                _sum = curr_l1.val + flag
            
                if _sum > 9:
                    new_node = ListNode(int(str(_sum)[-1]))
                    curr.next = new_node
                    curr = new_node
                    flag = 1
                else:
                    new_node = ListNode(_sum)
                    curr.next = new_node
                    curr = new_node
                    flag = 0

                curr_l1 = curr_l1.next
            if _sum > 9:
                new_node = ListNode(1)
                curr.next = new_node
        if curr_l2:
            while curr_l2 :
                _sum = curr_l2.val + flag
            
                if _sum > 9:
                    new_node = ListNode(int(str(_sum)[-1]))
                    curr.next = new_node
                    curr = new_node
                    flag = 1
                else:
                    new_node = ListNode(_sum)
                    curr.next = new_node
                    curr = new_node
                    flag = 0

                curr_l2 = curr_l2.next
            if _sum > 9:
                new_node = ListNode(1)
                curr.next = new_node


        return new_head.next

