class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=""
        longest_substring=0
        for character in s:
            if character in substring:
                substring=substring[substring.find(character)+1:]
            substring=substring+character
            if longest_substring < len(substring):
                longest_substring=len(substring)
        return longest_substring