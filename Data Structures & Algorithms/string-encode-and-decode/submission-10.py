class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded=""
        for string in strs:
            encoded+=f"{len(string)}#{string}"
        return encoded



    def decode(self, s: str) -> List[str]:
        res=[]
        pointer=0
        while pointer<len(s):
            delimiter=s.index("#",pointer)
            num=int(s[pointer:delimiter])
            pointer=delimiter+num+1
            res.append(s[delimiter+1:delimiter+num+1])
        return res
        

