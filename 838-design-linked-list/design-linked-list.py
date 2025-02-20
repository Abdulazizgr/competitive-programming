class ListNode:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.new_ls= None
        
    def get(self, index: int) -> int:
        curr = self.new_ls
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            idx += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.new_ls
        self.new_ls= new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.new_ls
        if curr is None:
            self.new_ls= new_node
            return 
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        new_node = ListNode(val)
        idx = 0
        if index == 0:
            new_node.next = self.new_ls
            self.new_ls= new_node
            return 
        curr = self.new_ls
        while curr:
            if index -1 == idx:
                new_node.next = curr.next
                curr.next = new_node
                return 
            curr = curr.next
            idx +=1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.new_ls is None or index < 0:
            return
        idx = 0
        if index == 0:
            self.new_ls= self.new_ls.next
            return 
        curr = self.new_ls
        while curr and curr.next:
            if index -1 == idx:
                curr.next = curr.next.next
                return 
            curr = curr.next
            idx +=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)