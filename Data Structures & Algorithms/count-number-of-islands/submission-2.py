class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        visited = set()
        def bfs(r,c):
            q = deque()
            
            q.append([r,c])
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col + dc
                    if nr < 0 or nr>= rows or nc< 0 or nc >= cols or grid[nr][nc] == "0" or (nr,nc) in visited:
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
