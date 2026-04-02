class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and self.minstack[-1] >= val:
            self.minstack.append(val)
        elif not self.minstack:
            self.minstack.append(val)
            
        

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
