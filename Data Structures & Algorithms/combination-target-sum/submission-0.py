class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

       

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                combo.append(nums[j])
                dfs(j, combo, total+ nums[j])
                combo.pop()

        dfs(0, [], 0)

        return res

            



            

        