class Solution:
    def isValid(self, s: str) -> bool:
        cto = {")": "(", "]" : "[", "}":"{"}
        stack = []

        for c in s:
            if c not in cto:
                stack.append(c)
            else:
                if not stack or stack.pop() != cto[c]:
                    return False
        return not stack
