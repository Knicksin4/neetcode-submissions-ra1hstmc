class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]

        majoity = 0
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            count += (1 if n == majority else -1)
        return majority

    

        