class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dp (row, col):
            prevrow = [0] * col
            if obstacleGrid[m-1][n-1] == 1: return 0
            prevrow[col - 1] = 1

            for r in range(row - 1, -1, -1):
                currow = [0] * col
                for c in range(col - 1, -1, -1):
                    if obstacleGrid[r][c] == 1:
                        currow[c] = 0
                    else:
                        if r == row - 1 and c == col - 1: 
                            currow[c] = 1
                        else:
                            right_val = currow[c + 1] if c + 1 < col else 0
                            down_val = prevrow[c] if r + 1 < row else 0
                            currow[c] = right_val + down_val
                prevrow = currow
            return prevrow[0]
        return dp(m, n)