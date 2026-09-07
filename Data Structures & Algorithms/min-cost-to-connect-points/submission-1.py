class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])

        minheap = [[0,0]]
        visit = set()
        res = 0
        mst = []

        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            mst.append([node, cost])
            visit.add(node)
            res += cost
            for neighbor, distance in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minheap, [distance, neighbor])

        return res