class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ans = []
        heapq.heapify(ans)
        hmap = {}

        for point in points:
            d = math.sqrt((point[0] * point[0]) + point[1] * point[1])
            heapq.heappush(ans,d)
            hmap.setdefault(d, []).append(point)

        while k >=1:
            k -=1
            p = heapq.heappop(ans)
            newpoint = hmap[p].pop()
            res.append(newpoint)

        return res
