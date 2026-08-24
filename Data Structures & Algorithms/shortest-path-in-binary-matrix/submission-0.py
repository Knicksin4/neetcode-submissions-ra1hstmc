class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        directions = [[1,0], [-1, 0], [1, 1], [-1, -1], [0, 1], [0, -1],[ 1, -1], [-1, 1]]

        def bfs(r,c):
            q = deque([(r, c, 1)])
            grid[r][c] = 1

            while q:
                row, col, path = q.popleft()
                if row == rows - 1 and col == cols - 1:
                    return path
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 1:
                        continue
                    grid[nr][nc] = 1
                    q.append((nr, nc, path + 1))
            return -1
        return bfs(0,0)