class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newnums = [-n for n in nums]
        heapq.heapify(newnums)

        while k >= 1:
            k -=1
            ans = heapq.heappop(newnums)
        return (ans * -1)
        