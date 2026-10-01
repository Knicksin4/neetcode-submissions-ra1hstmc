class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {}

        for i in range(n):
            adj[i] = []

        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)

        q = deque([0])
        visit = {0}


        while q:
            src = q.popleft()
            for des in adj[src]:
                if des not in visit:
                    visit.add(des)
                    q.append(des)

        return len(visit) == n
