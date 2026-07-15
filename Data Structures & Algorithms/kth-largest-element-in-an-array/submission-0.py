import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated_list=[-n for n in nums]
        heapq.heapify(negated_list)
        maxk=0
        for i in range(k):
            maxk=heapq.heappop(negated_list)
        return -maxk