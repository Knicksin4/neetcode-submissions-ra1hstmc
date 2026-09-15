class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtracking(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if ispali(s, i, j):
                    part.append(s[i:j+1])
                    backtracking(j + 1)
                    part.pop()

        def ispali(word, start, end):
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True
        backtracking(0)
        return res
