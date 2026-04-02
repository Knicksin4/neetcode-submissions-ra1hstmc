class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        trap = 0
        maxl, maxr = height[l], height[r]
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                trap += max(0, (maxl - height[l]))
            else:
                r -= 1
                maxr = max(maxr, height[r])
                trap += max(0, (maxr - height[r]))
            
        return trap

            
        