import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap=self.mapPopulator(nums)
        print(frequencyMap)
        return heapq.nlargest(k,frequencyMap,key=frequencyMap.get)


    def mapPopulator(self,nums: List[int])->dict:
        frequencyMap=dict()
        for num in nums:
            frequencyMap[num]=frequencyMap.get(num,0)+1
        return frequencyMap