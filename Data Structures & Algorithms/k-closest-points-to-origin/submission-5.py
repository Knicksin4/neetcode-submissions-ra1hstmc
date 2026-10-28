class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return []
        heap = []
        res = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heap.append([dist, point[0], point[1]])

        heapq.heapify(heap)

        while k > 0:
            closest = heapq.heappop(heap)
            res.append([closest[1], closest[2]])
            k -= 1

        return res
