class Solution:
    def isalpha(self, c):
            if (ord(c) >= ord("A") and ord(c) <= ord("Z") or
               ord(c) >= ord("a") and ord(c) <= ord("z") or
               ord(c) >= ord("0") and ord(c) <= ord("9")):
                return True
            else:
                return False

    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s)-1

        while l <r:
            while l < r and not self.isalpha(s[l]):
                l += 1
            while r > l and not self.isalpha(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        