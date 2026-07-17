from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree=[0]*numCourses
        adj_list=defaultdict(list)
        for prerequisite in prerequisites:
                in_degree[prerequisite[0]]+=1
                adj_list[prerequisite[1]].append(prerequisite[0])
        queue=deque()
        for course in range(numCourses):
            if in_degree[course]==0:
                queue.append(course)
        
        order=[]
        while queue:
            node=queue.popleft()
            order.append(node)
            if adj_list.get(node):
                for neighborg in adj_list.get(node):
                    in_degree[neighborg] -= 1 
                    if in_degree[neighborg]==0:
                        queue.append(neighborg)
        print(order)
        if len(order)==numCourses:
            return order
        else:
            return []