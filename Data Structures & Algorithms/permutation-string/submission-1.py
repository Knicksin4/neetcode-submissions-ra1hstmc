class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        s1count = {}
        s2count = {}

        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)

        matches = sum(1 for char in "abcdefghijklmnopqrstuvwxyz" if s1count.get(char, 0) == s2count.get(char, 0))

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            char_r = s2[r]
            old_count_r = s2count.get(char_r, 0)
            s2count[char_r] = old_count_r + 1
            if s1count.get(char_r, 0) == s2count[char_r]:
                matches += 1
            elif s1count.get(char_r, 0) == old_count_r:
                matches -= 1

            char_l = s2[l]
            old_count_l = s2count.get(char_l, 0)
            s2count[char_l] = old_count_l - 1
            if s1count.get(char_l, 0) == s2count[char_l]:
                matches += 1
            elif s1count.get(char_l, 0) == old_count_l:
                matches -= 1
            l += 1
        return matches == 26