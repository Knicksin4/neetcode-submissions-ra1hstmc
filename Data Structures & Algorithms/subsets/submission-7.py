class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        self.helper(0, curr, res, nums)
        return res

    def helper(self, i, curr, res, nums):
        if i >= len(nums):
            res.append(curr.copy())
            return

        curr.append(nums[i])
        self.helper(i+1, curr, res, nums)

        curr.pop()
        self.helper(i+1, curr, res, nums)



        