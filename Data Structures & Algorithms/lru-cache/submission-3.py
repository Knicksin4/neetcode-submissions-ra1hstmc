class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next = nxt
        node.prev = prv
        

    def remove(self, node):
        nxt, prv = node.next, node.prev
        nxt.prev, prv.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        
