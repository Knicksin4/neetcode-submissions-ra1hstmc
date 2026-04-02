class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord("a")] += 1
            if tuple(freq) not in hmap:
                hmap[tuple(freq)] = [s]
            else:
                hmap[tuple(freq)].append(s)
        return hmap.values()

            


        