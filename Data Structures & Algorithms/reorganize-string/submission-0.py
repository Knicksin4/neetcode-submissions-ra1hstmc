class Solution:
    def reorganizeString(self, s: str) -> str:
        countmap = Counter(s)

        maxheap = [(-cnt, char) for char, cnt in countmap.items()]
        heapq.heapify(maxheap)

        res = ""
        previous = None # previous removal from heap

        while maxheap or previous:
            if previous and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1

            # set current as the next previous before updating previous back into heap
            current = (cnt, char) if cnt < 0 else None

            # ADD PREVIOUS BACK
            if previous:
                heapq.heappush(maxheap, previous)

            # set previous
            previous = current
        return res
