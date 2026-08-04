class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        i1 = 0
        i2 = 0            

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                new.append(nums1[i1])
                i1 += 1
            else:
                new.append(nums2[i2])
                i2 += 1

        while i1 < len(nums1):
            new.append(nums1[i1])
            i1 += 1
        while i2 < len(nums2):
            new.append(nums2[i2])
            i2 += 1

        n = len(new)
        if n % 2 == 1:
            return float(new[n // 2])
        else:
            return (new[n // 2 - 1] + new[n // 2]) / 2.0