# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            sub = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    sub.append(node.val)
            if sub:
                res.append(sub)
        return res
            


        