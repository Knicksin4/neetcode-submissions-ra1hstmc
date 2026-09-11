class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board) 
        COL = len(board[0])

        wordlen = len(word)

        def backtrack(row, col, wordsize):
            if wordsize == wordlen:
                return True
            if row >= ROW or col >= COL or row < 0 or col < 0 or board[row][col] == "." or word[wordsize] != board[row][col]:
                return False

            board[row][col] = "."

            res = (backtrack(row + 1, col, wordsize + 1) or backtrack(row - 1, col, wordsize + 1) or backtrack(row, col + 1, wordsize + 1) or backtrack(row, col -1, wordsize + 1))

            board[row][col] = word[wordsize]
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack(r,c,0):
                    return True
        return False

        
                

        