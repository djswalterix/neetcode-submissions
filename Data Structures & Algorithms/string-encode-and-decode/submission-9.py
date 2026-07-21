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
        print(s)
        while pointer<len(s):
            delimiter=s.index("#",pointer)
            print(delimiter,"delimiter")
            num=int(s[pointer:delimiter])
            pointer=delimiter+num+1
            print (num)
            print(s[delimiter+1:delimiter+num+1],"s[delimiter:delimiter+num]")
            res.append(s[delimiter+1:delimiter+num+1])
        return res
        

