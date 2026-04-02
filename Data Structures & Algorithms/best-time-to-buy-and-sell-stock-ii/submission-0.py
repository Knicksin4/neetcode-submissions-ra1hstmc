class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxprofit = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                profit = nums[i] - nums[i-1]
                ans += profit                
        return ans


        