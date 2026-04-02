class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # two dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        lastnode = self.tail.prev
        lastnode.next = new_node
        new_node.prev = lastnode
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        firstnode = self.head.next

        firstnode.prev = new_node
        new_node.next = firstnode
        new_node.prev = self.head
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        lastnode = self.tail.prev
        value = lastnode.val

        before = lastnode.prev
        before.next = self.tail
        self.tail.prev = before

        return value

        

    def popleft(self) -> int:
        
        if self.isEmpty():
            return -1
        firstnode = self.head.next
        second_node = firstnode.next

        value = firstnode.val

        second_node.prev = self.head
        self.head.next = second_node
        return value
        
