# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot: return True
        if not root:
            return False

        if self.sameTree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
        

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False
