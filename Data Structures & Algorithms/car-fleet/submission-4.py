class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position,speed)]

        stack = []
        cars.sort(reverse=True)

        for p,s in cars:
            stack.append((target-p) /s)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        