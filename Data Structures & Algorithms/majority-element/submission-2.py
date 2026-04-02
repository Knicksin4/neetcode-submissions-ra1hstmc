class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        half = len(nums)//2 + 1
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1
            if hmap[num] >= half:
                return num
        return

        