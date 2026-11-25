class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj:
            return False
        if dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def _dfs(curr):
            if curr == dst:
                return True
            visited.add(curr)
            for n in self.adj.get(curr, []):
                if n not in visited:
                    if _dfs(n):
                        return True
            return False
        return _dfs(src)