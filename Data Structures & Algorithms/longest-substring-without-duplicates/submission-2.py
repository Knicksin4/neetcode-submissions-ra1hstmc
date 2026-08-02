class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        l = 0
        myset = set()

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            res = max(res, r-l +1)

        return res



            

        