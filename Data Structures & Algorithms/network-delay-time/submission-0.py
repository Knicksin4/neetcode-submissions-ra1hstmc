class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        # times[i] = (source, destination, wieght)
                    
        for source, destination, weight in times:
            adj[source].append((destination, weight))

        minheap = [ [0, k]]
        shortest = {}

        while minheap:
            weight, target = heapq.heappop(minheap)
            if target in shortest:
                continue
            shortest[target] = weight

            for next_target, next_weight in adj[target]:
                if next_target not in shortest:
                    heapq.heappush(minheap, (weight + next_weight, next_target))
        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1