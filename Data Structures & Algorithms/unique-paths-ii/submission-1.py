class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        def dp (row, col):
            cache = [0] * n
            cache[n-1] = 1
            for r in reversed(range(m)):
                for c in reversed(range(n)):
                    if obstacleGrid[r][c]:
                        cache[c] = 0
                    elif c < n -1:
                        cache[c] = cache[c] + cache[c + 1]
            return cache[0]


            
        return dp(m, n)