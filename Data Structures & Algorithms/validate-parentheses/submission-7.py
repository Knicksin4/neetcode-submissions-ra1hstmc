class Solution:
    def isValid(self, s: str) -> bool:
        otc = {")":"(", "]":"[", "}":"{",}
        stack = []

        for c in s:
            if c not in otc:
                stack.append(c)
            else: 
                if not stack:
                    return False
                top = stack.pop()
                if top != otc[c]:
                    return False
        return not stack

            
        