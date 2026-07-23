class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            else:
                myset.add(nums[i])
            if len(myset) > k:
                myset.remove(nums[i-k])
        return False