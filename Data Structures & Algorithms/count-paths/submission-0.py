class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(rows, cols):
            prevrow = [0] * cols
        
            for r in range(rows -1, -1, -1):
                currow = [0] * cols
                currow[cols -1] = 1

                for c in range(cols -2, -1, -1):
                    currow[c] = prevrow[c] + currow[c + 1]
                prevrow = currow
            return currow[0]
        return dp(m, n)
