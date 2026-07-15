import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heapq_stones=[-stone for stone in stones]
        heapq.heapify(max_heapq_stones)
        while len(max_heapq_stones)>1:
            stoneA=- heapq.heappop(max_heapq_stones)
            stoneB=- heapq.heappop(max_heapq_stones)
            smashed_stones=stoneA-stoneB
            if smashed_stones!=0:
                heapq.heappush(max_heapq_stones,-smashed_stones)
        if not max_heapq_stones:
            return 0
        return -max_heapq_stones[0]