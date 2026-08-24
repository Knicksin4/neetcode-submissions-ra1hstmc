class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]

        for _ in range(n):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
        return dp[1]


