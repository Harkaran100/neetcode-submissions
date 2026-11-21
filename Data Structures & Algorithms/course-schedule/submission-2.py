class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []

        for course, required in prerequisites:
            prereq[required].append(course)
        
        visiting = set()
        done = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True
            visiting.add(course)
            for required in prereq[course]:
                if not dfs(required):
                    return False
            visiting.remove(course)
            done.add(course)
            return True
        for course in prereq:
            if not dfs(course):
                return False
        return True

