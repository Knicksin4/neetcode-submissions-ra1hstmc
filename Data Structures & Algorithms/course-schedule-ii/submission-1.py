class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereqs = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        output =[]

        visited = set()
        current = set()

        def dfs(course):
            if course in current:
                return False
            if course in visited: 
                return True

            current.add(course)

            for c in prereqs[course]:
                if not dfs(c):
                    return False
            current.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output

        
        