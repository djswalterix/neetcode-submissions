class Solution: #1 5 6 9 target 7
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        left=0

        while(left<right):

            if  numbers[right]+numbers[left]< target:
                left+=1
            if  numbers[right]+numbers[left]> target:
                right-=1 
            if  numbers[right]+numbers[left] == target:
                return [left+1,right+1]          
            