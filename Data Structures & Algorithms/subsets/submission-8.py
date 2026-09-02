class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        def helper(i, curr, res, nums):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            helper(i+1, curr, res, nums)

            curr.pop()
            helper(i+1, curr, res, nums)
        helper(0, curr, res, nums)
        return res        