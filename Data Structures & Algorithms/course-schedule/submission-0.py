class Solution:
    def canFinish(self, numcourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numcourses)}

        for course, pre in prerequisites:
            premap[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if premap[course] == []:
                return True

            visited.add(course)

            for prereq in premap[course]:
                cantake = dfs(prereq)
                if not cantake:
                    return False
            visited.remove(course)
            premap[course] = []
            return True
        for crs in range(numcourses):
            if not dfs(crs): return False
        return True

                
        