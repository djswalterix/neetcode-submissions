class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict=self.build_dict_with_count(s)
        t_dict=self.build_dict_with_count(t)
        if s_dict==t_dict:
            return True
        return False
        

    def build_dict_with_count(self,input_string:str)->dict:
        dict_with_count=dict()
        for characther in input_string:
            dict_with_count[characther]=dict_with_count.get(characther,0)+1
        return dict_with_count