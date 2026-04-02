class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        l = 0
        myset = set()
        longest = 0

        for r in range(len(nums)):
            while myset and nums[r] in myset:
                myset.remove(nums[l])
                l += 1
            myset.add(nums[r])
            longest = max(longest,(r-l+1))
        return longest
            
                

                