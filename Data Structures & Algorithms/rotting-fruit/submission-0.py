class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        time = 0
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:

            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        return -1
                    

                

        