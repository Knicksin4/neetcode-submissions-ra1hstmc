class Node:
    def __init__(self, is_file=False):
        self.children = {}
        self.content = ""
        self.is_file = is_file
class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        parts = path.split("/")
        curr = self.root

        for i in range(1,len(parts)):
            name = parts[i]
            if not name:
                continue
            if name in curr.children:
                curr = curr.children[name]
        file_present = curr.is_file
        if file_present:
            return [parts[-1]]
        else:
            return sorted(curr.children.keys())
        

    def mkdir(self, path: str) -> None:
        parts = path.split("/")
        curr = self.root

        for i in range(1, len(parts)):
            name = parts[i]
            if not name:
                continue
            if name not in curr.children:
                curr.children[name] = Node(False)
            curr = curr.children[name]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split("/")
        curr = self.root

        for i in range(1, len(parts)):
            name = parts[i]
            if not name:
                continue
            if name not in curr.children:
                is_last = (i == len(parts) - 1)
                curr.children[name] = Node()
            curr = curr.children[name]
        
        curr.is_file = True
        curr.content += content

        

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split("/")
        curr = self.root

        for i in range(1, len(parts)):
            name = parts[i]
            curr = curr.children[name]
        return curr.content

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
