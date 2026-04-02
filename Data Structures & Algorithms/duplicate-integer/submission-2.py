class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i,n in enumerate(nums):
            if n in hmap:
                return True
            hmap[n] = i
        return False


         