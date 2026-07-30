from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)


        for word in strs:
            nums = [0] * 26
            for char in word:
                nums[ord(char) - ord("a")] += 1
            anagrams[tuple(nums)].append(word)
        return list(anagrams.values())
