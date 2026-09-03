class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        resset = set()

        def permute(i):
            if i == len(nums):
                return [[]]

            resperm = []
            perms = permute(i + 1)

            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    if tuple(pcopy) not in resset:
                        resperm.append(pcopy)
                        resset.add(tuple(pcopy))
            return resperm

        return permute(0)


        