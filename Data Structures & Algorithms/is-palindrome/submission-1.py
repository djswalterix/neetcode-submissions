class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for char in s.lower():
            if char.isalpha()|char.isnumeric():
                string+=char
        print(string)


        for i in range (0, int(len(string)/2)):
            print(string[i]," left")
            print(string[len(string)-i-1]," right")
            if string[i]!=string[len(string)-i-1]:
                return False
        return True