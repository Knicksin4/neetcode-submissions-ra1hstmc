class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest =0
       
        for n in myset:
            if n-1 not in myset:
                long = 1
                while n + long in myset:
                    long += 1
                longest = max(longest, long)
        return longest
        