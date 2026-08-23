class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):

            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                        continue

                    grid[nr][nc] = "0"
                    q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        return count
