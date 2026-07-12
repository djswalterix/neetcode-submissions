class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        best_so_far=0
        count=dict()
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            while (right-left+1)-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            best_so_far=max(right-left+1,best_so_far)
        return best_so_far