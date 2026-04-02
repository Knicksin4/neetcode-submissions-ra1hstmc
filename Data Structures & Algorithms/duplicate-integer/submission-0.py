class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                return True
            hmap[nums[i]] = i

        return False


         