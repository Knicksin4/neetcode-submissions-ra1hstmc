class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        


    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newarr = [0] * self.capacity

        for i in range(self.size):
            newarr[i] = self.arr[i]
        self.arr = newarr

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
