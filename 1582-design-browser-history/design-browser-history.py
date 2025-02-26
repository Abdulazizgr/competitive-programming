class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()  
        self.tail = ListNode()  
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, val: str) -> ListNode:
        node = ListNode(val)

        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail

        node.next = self.tail
        self.tail.prev = node

        return node  

class BrowserHistory:
    def __init__(self, homepage: str):
        self.dll = DoubleLinkedList()
        self.current = self.dll.add(homepage)  

    def visit(self, url: str) -> None:
        
        new_node = ListNode(url)

     
        self.current.next = self.dll.tail
        self.dll.tail.prev = self.current

       
        self.current.next = new_node
        new_node.prev = self.current
        new_node.next = self.dll.tail
        self.dll.tail.prev = new_node

        self.current = new_node  

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != self.dll.head:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != self.dll.tail:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)