class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in differences:
                return [differences[diff], i]
            else:
                differences[n] = i
        