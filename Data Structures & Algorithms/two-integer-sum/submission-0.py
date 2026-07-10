class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict=dict()
        for counter in range(0,len(nums)):
            complement=target-nums[counter]
            if nums[counter] in seen_dict:
                return [seen_dict.get(nums[counter]),counter]
            seen_dict[complement]=counter
