class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            hours = (target - p) / s
            if not stack or hours > stack[-1]:
                stack.append(hours)

        return len(stack)