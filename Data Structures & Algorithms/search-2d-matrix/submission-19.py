class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #example 
        left=0
        len_cols=len(matrix[0])
        len_rows=len(matrix)
        right=(len(matrix)*len(matrix[0]))-1
        while left<=right:
            middle=(left+right)//2
            val=matrix[middle//len_cols][middle%len_cols]
            if val==target:
                return True
            elif val<target:
                left=middle+1
            else:
                right=middle-1
        return False
