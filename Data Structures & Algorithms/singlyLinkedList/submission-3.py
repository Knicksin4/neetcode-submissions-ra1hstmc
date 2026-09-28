class ListNode:
    def __init__(self, val, nextnode=None):
        self.val = val
        self.next = nextnode

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next
        if curr and i == index:
            return curr.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        newhead = ListNode(val, self.head)
        self.head = newhead

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1
        if not curr or not curr.next:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        newarr = []
        curr = self.head
        while curr:
            newarr.append(curr.val)
            curr = curr.next
        return newarr