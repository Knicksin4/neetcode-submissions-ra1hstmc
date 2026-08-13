class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = collections.Counter(tasks)
        q = deque()
        time = 0

        heap = [ -cnt for cnt in count.values()]
        heapq.heapify(heap)
        

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap) 
                if cnt:
                    q.append([cnt, n + time])
            if q and q[0][1] == time:
                heapq.heappush(heap, (q.popleft()[0]))

        return time
