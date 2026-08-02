class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(a+b)

            elif token == "-":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b-a)

            elif token == "*":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(a*b)

            elif token == "/":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b/a)
            
            else:
                stack.append(token)
        return int(stack[-1])