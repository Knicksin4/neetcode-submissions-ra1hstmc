class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1, 0], [0, 1], [0 ,-1]]
        maxa = 0

        def bfs(r, c):

            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr,nc))
                    res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxa = max(maxa, area)

        return maxa