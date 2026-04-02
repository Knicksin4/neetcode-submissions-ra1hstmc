class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # half = len(nums)//2 + 1
        # hmap = defaultdict(int)

        # for num in nums:
        #     hmap[num] += 1
        #     if hmap[num] >= half:
        #         return num
        # return
        res = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -=1
        return res




        