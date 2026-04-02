class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = []
        for stone in stones:
            rocks.append(stone * -1)

        heapq.heapify(rocks)
        while len(rocks) > 1:
            x = abs(heapq.heappop(rocks))
            y = abs(heapq.heappop(rocks))
            if x == y:
                continue
            elif x > y:
                x-=y
                x = x * -1
                heapq.heappush(rocks, x)
            else:
                y-=x
                y = y * -1
                heapq.heappush(rocks, y)
        return 0 if not rocks else -1 * rocks[0]

        