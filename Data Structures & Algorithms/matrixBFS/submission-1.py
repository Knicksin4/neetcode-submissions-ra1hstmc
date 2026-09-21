class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        visit = set()
        q = deque(())
        q.append((0,0))
        visit.add((0,0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr,dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or 
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r+dr][c+dc] == 1):

                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1
