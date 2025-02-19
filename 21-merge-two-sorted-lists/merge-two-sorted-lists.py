# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        new_node =ListNode(-1)
        curr = new_node
        while list1 and list2:
            if list1.val > list2.val:
                new_nod = ListNode(list2.val)
                curr.next = new_nod
                curr = new_nod
                list2 = list2.next
            else:
                new_nod = ListNode(list1.val)
                curr.next = new_nod
                curr = new_nod
                list1 = list1.next
        if list1 :
            curr.next = list1
        else:
            curr.next = list2

        return new_node.next





            # def insert_at_end(self, data):
            #     new_node = Node(data)

            #     if self.head is None:
            #         self.head = new_node
            #     else:
            #         curr = self.head
            #         while curr.next:
            #             curr = curr.next
            #         curr.next = new_node
            #     curr_1 = list1
            #     curr_2 = list2
            #     while curr_1 and cuu_2:
            #         if curr_1.val > curr_2.val:
            #             insert_at_end(curr_1.val)
            #             curr_1 = curr_1.next
            #         elif curr_1.val == curr_2.val:
            #             insert_at_end(curr_2.val)
            #             insert_at_end(curr_1.val)
            #             curr_2 = curr_2.next
            #             curr_1 = curr_1.next

            #         else:
            #             insert_at_end(curr_2.val)
            #             curr_2 = curr_2.next
                    
                   
            # return 
        


