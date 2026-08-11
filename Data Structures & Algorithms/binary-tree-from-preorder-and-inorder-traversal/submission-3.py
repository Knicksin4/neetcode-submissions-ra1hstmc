# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.index = 0

        cache = {v:i for i,v in enumerate(inorder)}

        def dfs(start, end):
            if start > end:
                return None

            root = TreeNode(preorder[self.index])
            self.index += 1
            mid = cache[root.val]

            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)

            return root
        return dfs(0, len(inorder) - 1)