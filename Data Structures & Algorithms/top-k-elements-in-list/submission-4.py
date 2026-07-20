from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count=Counter(nums)
        return heapq.nlargest(k,freq_count,key=freq_count.get)