class RandomizedSet:

    def __init__(self):
        self.random = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.random:
            index = self.random[val]
            last = self.nums[-1]
            self.nums[index] = last
            self.random[last] = index
            self.nums.pop()
            del self.random[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.nums)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()