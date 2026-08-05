class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = {}

        for i,n in enumerate(nums):
            if n in seen:
                return n
            seen[n] = i
            
        