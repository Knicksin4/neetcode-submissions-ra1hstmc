class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()

        def bfs(row, col,):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visit or grid[row][col] == -1:
                return

            visit.add((row,col))
            queue.append([row,col])
        for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        queue.append([r,c])
                        visit.add((r,c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                bfs(row + 1,col)
                bfs(row - 1,col)
                bfs(row,col + 1)
                bfs(row,col - 1)
            dist += 1