class Node:
    def __init__(self, is_file=False):
        self.children = {}
        self.content = ""
        self.is_file = is_file
class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        curr = self.root
        parts = path.split("/")
        
        if path != "/":
            for i in range(1, len(parts)):
                curr = curr.children[parts[i]]
            
            if curr.is_file:
                return [parts[-1]]
            
        return sorted(curr.children.keys())

        

    def mkdir(self, path: str) -> None:
        curr = self.root
        parts = path.split("/")
        
        for i in range(1, len(parts)):
            if parts[i] not in curr.children:
                curr.children[parts[i]] = Node(False)
            curr = curr.children[parts[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        parts = filePath.split("/")

        for i in range(1, len(parts)):
            name = parts[i]
            if name not in curr.children:
                is_last = (i == len(parts) - 1)
                curr.children[name] = Node(is_last)
            curr = curr.children[name]

        curr.content += content

            
        

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        parts = filePath.split("/")
        for i in range(1, len(parts)):
            curr = curr.children[parts[i]]
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
