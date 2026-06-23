# given  array prereq, where prereq[i] = [a,b]
# this indicates if you want to take course a must take b first
# you are required to take numCourses
# return the valid ordering of courses you have to take
# if multiple, return any, in none, return empty array

 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: create graph and indegree list
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        # Step 2: fill graph and indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 3: add all courses with no prerequisites to queue
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # Step 4: process available courses
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 5: if we took all courses, return order
        if len(order) == numCourses:
            return order

        # Otherwise, there was a cycle
        return []