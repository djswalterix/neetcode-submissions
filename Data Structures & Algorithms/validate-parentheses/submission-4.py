class Solution:
    def isValid(self, s: str) -> bool:
        open_stack=[]
        pairs = {')': '(', ']': '[', '}': '{'}
        if len(s)%2!=0:
            return False
        for bracket in s:
            if bracket not in pairs:
                open_stack.append(bracket)
            else:
                if open_stack:
                    last_stack=open_stack.pop()
                    if last_stack !=pairs[bracket]:
                        return False
                else:
                    return False
        return len(open_stack)==0
        