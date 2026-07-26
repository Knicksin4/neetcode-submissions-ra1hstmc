class TrieNode:
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1
class FileSystem:

    def __init__(self):
        self.root = TrieNode("")
        

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split("/")
        curr = self.root
        for i in range(1, len(parts)):
            name = parts[i]
            if name not in curr.map:
                if i == len(parts)-1:
                    curr.map[name] = TrieNode(name)
                else:
                    return False
            curr = curr.map[name]
        if curr.value != -1:
            return False
        curr.value = value
        return True
                     
    def get(self, path: str) -> int:
        parts = path.split("/")
        curr = self.root
        for i in range(1, len(parts)):
            if parts[i] not in curr.map:
                return -1
            curr = curr.map[parts[i]]
        return curr.value
            
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
