class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                index,_ = stack.pop()
                res[index] = i - index
            stack.append((i,n))
        return res
        