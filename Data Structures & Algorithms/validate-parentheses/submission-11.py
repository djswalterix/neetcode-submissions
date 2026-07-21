class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        if len(s)%2!=0:
            return False
        stack_open=[]
        for Parentheses in s:
            print(Parentheses,Parentheses in pairs)
            if Parentheses in pairs:
                if not stack_open:
                    return False
                last_p=stack_open.pop()
                if last_p!=pairs[Parentheses]:
                    return False
            else:
                stack_open.append(Parentheses)
        return not stack_open