class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        ans = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            possible = 0

            for pile in piles:
                possible += math.ceil(pile / mid)
            if possible <= h:
                ans = min(ans,mid)
                upper = mid - 1
            elif possible > h:
                lower = mid + 1
        return ans
                
                



        