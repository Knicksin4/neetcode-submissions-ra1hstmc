class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adj = {}
        for i in range(n + 1):
            adj[i] = []
        for src, dst , weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])

        minheap = []
        for dst, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, dst])
        
        visit = set()
        visit.add(0)
        mst = []
        total = 0

        while minheap:
            weight, node, nextnode = heapq.heappop(minheap)
            if nextnode in visit:
                continue
            visit.add(nextnode)
            mst.append([node, nextnode, weight])
            total += weight
            for neighbor, nextweight in adj[nextnode]:
                if neighbor not in visit:
                    heapq.heappush(minheap, [nextweight, nextnode, neighbor])
        return total if len(visit) == n else -1
        

            



        
        