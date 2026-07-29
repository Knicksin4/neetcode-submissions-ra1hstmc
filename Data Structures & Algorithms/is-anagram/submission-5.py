class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrams = {}
        for c in s:
            if c not in anagrams:
                anagrams[c] = 1
            else:
                anagrams[c] += 1
        
        for m in t:
            if m not in anagrams:
                return False
            else:
                anagrams[m] -= 1
                if anagrams[m] == 0:
                    del anagrams[m]
        return len(anagrams) ==0

        