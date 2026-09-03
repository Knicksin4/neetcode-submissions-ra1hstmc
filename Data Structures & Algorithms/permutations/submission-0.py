class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # perms = [[]]

        def permutation(i , nums):
            if i == len(nums):
                return [[]]

            res = []
            perms = permutation(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res

        return permutation(0, nums)
        