class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)

        longest = 0

        for num in myset:
            if num - 1 not in myset:
                length = 1
                while length + num in myset:
                    length += 1
                longest = max(longest, length)
        return longest

        