class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereqs = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        visited = set()
        current = set()
        output = []

        def dfs(course):
            if course in current:
                return False
            if course in visited:
                return True

            current.add(course)

            for crs in prereqs[course]:
                if not dfs(crs):
                    return False
            visited.add(course)
            current.remove(course)
            output.append(course)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output