class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = {}

    def addword(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addword(word)

        visit = set()
        res = set()

        rows, cols = len(board), len(board[0])

        def dfs(row, col, node, word):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit or board[row][col] not in node.children:
                return

            visit.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isword:
                res.add(word)
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visit.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")
        return list(res)