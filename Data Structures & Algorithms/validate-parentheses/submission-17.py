class Solution:
    def isValid(self, s: str) -> bool:
        ctoa = { ")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in ctoa:
                if not stack or stack[-1] != ctoa[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
                
