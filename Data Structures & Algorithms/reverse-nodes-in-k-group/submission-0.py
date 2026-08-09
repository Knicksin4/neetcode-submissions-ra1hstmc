# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        beforek = dummy

        while True:
            knode = self.getk(beforek, k)
            if not knode:
                break
            groupnext = knode.next

            prev, curr = knode.next, beforek.next
            while curr != groupnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = beforek.next
            beforek.next = knode
            beforek = tmp
        return dummy.next

    def getk(self, curr, k):
        while curr and k >0:
            curr = curr.next
            k -= 1
        return curr
