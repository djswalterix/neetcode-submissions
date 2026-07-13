class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer=int((len(nums)-1)/2)
        print("len(nums)",len(nums))
        last_pointer=None
        count=0
        print("pointer ",pointer," nums[pointer] ",nums[pointer]," target ",target,"last_pointer",last_pointer)

        while pointer>=0 and pointer<=len(nums)-1:
            count+=1
            print("pointer ",pointer," nums[pointer] ",nums[pointer]," target ",target,"last_pointer",last_pointer)
            if nums[pointer]==target:
                return pointer
            if nums[pointer]>target:
                pointer=pointer-int(((len(nums)+1)-pointer)/2)
            if nums[pointer]<target:
                pointer=pointer+int(((len(nums)+1)-pointer)/2)
            if last_pointer==pointer or count==5:
                return -1
            else:
                last_pointer=pointer
        return -1