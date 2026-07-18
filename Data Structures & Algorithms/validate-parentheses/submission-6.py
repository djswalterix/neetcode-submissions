class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for bracket in s:
            print(bracket)
            print(bracket not in pairs)
            if bracket not in pairs: #check if the bracket is not a closing one 
                stack.append(bracket) # if its opener get's added to the stack
            else: #
                if stack:
                    last_item=stack.pop() #if it's a closer we get last stack item and we check that is the relative opener of this closer
                    print(last_item,"last item")
                    if last_item != pairs[bracket]:
                        return False
                else:
                    return False
        if len(stack)==0: #  we check len to be sure each opener has been closed
            return True
        else:
            return False
        
        