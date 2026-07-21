class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=1
        max_valid_window=0
        while end<=len(s):
            current_set=set(s[start:end])
            if len(current_set)==end-start:
                end+=1
                max_valid_window=max(max_valid_window,end-1-start)

            else:
                max_valid_window=max(max_valid_window,end-1-start)
                start+=1
        return max_valid_window
