class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def build_dict(s):
            chars_with_count={}
            for ch in s:
                chars_with_count[ch]=chars_with_count.get(ch,0)+1
            return chars_with_count
        
        if len(s)!=len(t):
            return False
        s_dict=build_dict(s)
        t_dict=build_dict(t)
        if s_dict==t_dict:
            return True
        else:
            return False