class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        for c in s:
            if c not in hmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    val = stack.pop()
                    if val != hmap[c]:
                        return False
        return not stack

        