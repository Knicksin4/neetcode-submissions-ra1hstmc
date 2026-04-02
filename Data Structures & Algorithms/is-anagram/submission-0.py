class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        dmap = {}
        for c in s:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 0
        
        for c in t:
            if c in dmap:
                dmap[c] += 1
            else:
                dmap[c] = 0
        return hmap == dmap


        




        