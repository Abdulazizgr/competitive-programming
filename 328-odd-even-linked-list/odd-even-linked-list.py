# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        temp = None
        count = 0
        while curr:
            count +=1
            tail = curr
            curr = curr.next
       
      
        count = count //2 
        current = head
  
        while count > 0 and current and current.next :
            temp = current.next.val
            tail.next = ListNode(temp)
            tail = tail.next
            current.next = current.next.next
            current = current.next
            count -= 1
           
        return head
