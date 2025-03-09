class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.index = 0
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if len(self.stack1) - self.index == 1:
            self.stack2.append(x)

    def pop(self) -> int:
        num = self.stack2.pop()
        self.index += 1
        if self.index < len(self.stack1):
            self.stack2.append(self.stack1[self.index])
        return num
        
    def peek(self) -> int:
        if self.stack2:
            return self.stack2[0]
    
    def empty(self) -> bool:
        return len(self.stack1) == self.index
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()