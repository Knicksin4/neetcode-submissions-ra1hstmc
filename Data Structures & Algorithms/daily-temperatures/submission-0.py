class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, val = stack.pop()
                res[i] = index - i
            else:
                
                stack.append((index,temp))
        return res
            

       
        