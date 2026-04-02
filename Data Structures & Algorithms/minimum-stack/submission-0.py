class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.stack and not self.minstack:
            self.minstack.append(val)

        elif self.stack and self.minstack and val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)

        

        

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
        if self.minstack and val == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
