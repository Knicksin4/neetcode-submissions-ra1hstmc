class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x,y = point[0], point[1]
            distance = math.sqrt((x * x) + (y * y))
            distances.append((distance,[x,y]))

        heapq.heapify(distances)
        res = []

        for _ in range(k):
            point = heapq.heappop(distances)
            res.append(point[1])

        return res


       

        