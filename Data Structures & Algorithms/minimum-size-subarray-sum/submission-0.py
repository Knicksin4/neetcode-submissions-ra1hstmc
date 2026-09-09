# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums = [1, 3, 4, 5, 6, 8] target = 14

        left = 0
        n = len(nums)
        total = 0
        minsubarray = float("inf")

        for r in range(n):
            total += nums[r]
            while total >= target:
                minsubarray = min(minsubarray, (r-left) + 1)
                total -= nums[left]
                left += 1
        return minsubarray if minsubarray != float("inf") else 0
        