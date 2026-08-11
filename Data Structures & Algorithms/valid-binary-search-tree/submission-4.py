# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lowbound, upperbound):
            if not node:
                return True
            if node.val <= lowbound or node.val >= upperbound:
                return False
            return (dfs(node.left, lowbound, node.val) and dfs(node.right, node.val, upperbound))
        
        return dfs(root, float("-infinity"), float("infinity"))
            
        