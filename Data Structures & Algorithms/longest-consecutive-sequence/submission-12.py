class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0

        for n in myset:
            if (n - 1) not in myset:
                curr = 1
                while n + curr in myset:
                    curr += 1
                
                longest = max(longest, curr)
        return longest



        