class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2 4 5.   7
        #n 2 comp 5 
        #comp[5]=0
        if not nums:
            return []
        comps={}
        for i in range(len(nums)):
            looking_for=target-nums[i]
            print(looking_for,"looking_for")
            print(comps.get(looking_for),"comps.get(looking_for)")
            if looking_for in comps:
                return [comps.get(looking_for),i]
            comps[nums[i]]=i
            print(comps,"comps")
        return []