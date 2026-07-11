class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=1
        right_product=1
        output=[]
        for i in range(0, len(nums)):
            output.append(left_product)
            left_product=left_product*nums[i]
        for j in range(len(nums)-1,-1,-1):
            output[j]=output[j]*right_product
            right_product=right_product*nums[j]
        return output