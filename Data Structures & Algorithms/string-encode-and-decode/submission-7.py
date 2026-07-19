class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for string in strs:
            encoded+=str(len(string))+"#"+string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=int(s.find("#",i))+1
            n=s[i:j-1]
            word=s[j:j+int(n)]
            decoded.append(word)
            i=j+len(word)
        return decoded
