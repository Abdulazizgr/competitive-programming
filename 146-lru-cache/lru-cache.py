class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        self.tail.prev = node
        node.next = self.tail

    def remove(self, node):
        next_node = node.next
        previous_node = node.prev

        next_node.prev = previous_node
        previous_node.next = next_node

    def getHead(self):
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.order = DoubleLinkedList()
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.order.remove(node)
        self.order.add(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.order.remove(node)
            self.order.add(node)

        else:
            if self.capacity == len(self.cache):
                least_used = self.order.getHead()
                self.order.remove(least_used)
                
                del self.cache[least_used.key]

            new_node = Node(key, value)
            self.order.add(new_node)
            self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)