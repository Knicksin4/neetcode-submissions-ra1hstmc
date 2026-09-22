class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = {}
        for i in range(n):
            adj[i] = []

        for s, d, w in edges:
            adj[s].append([w, d])

        shortest = {}

        minheap = [[0, src]]

        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in shortest:
                continue
            shortest[node] = weight

            for nextweight, nextnode in adj[node]:
                if nextnode not in shortest:
                    heapq.heappush(minheap, [weight + nextweight, nextnode])
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
