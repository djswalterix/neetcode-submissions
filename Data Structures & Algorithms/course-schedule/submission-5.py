class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c: [] for c in range(numCourses)}
        for course in prerequisites:
            graph[course[0]].append(course[1])
        print (graph)
        explored=set()
        exploring=set()

        def dfs(course):
            if course in exploring:
                return False
            if course in explored:
                return True
            
            exploring.add(course)
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            exploring.remove(course)
            explored.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

