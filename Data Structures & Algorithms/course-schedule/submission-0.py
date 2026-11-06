class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseRequirements = {}
        visiting = set()

        def dfs(course):
            if course in visiting: # cycle
                return False
            if courseRequirements[course] == []: # emptty
                return True
            # continue traversal
            visiting.add(course)

            for prereqs in courseRequirements[course]:
                if not dfs(prereqs):
                    return False

            visiting.remove(course)
            courseRequirements[course] = []
            return True

        
        # make prereq hash
        for course in range(numCourses):
            courseRequirements[course] = []

        for course, prereq in prerequisites:
            courseRequirements[course].append(prereq)

        # now that hash is made, go through hash in dfs
        for course in courseRequirements:
            if not dfs(course):
                return False
        return True
        
        

        