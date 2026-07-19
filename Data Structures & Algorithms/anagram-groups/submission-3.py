class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        group_anagram={}
        for string in strs:
            key="".join(sorted(string))
            if key not in group_anagram:
                group_anagram[key]=[]
            group_anagram[key].append(string)
        return list(group_anagram.values())