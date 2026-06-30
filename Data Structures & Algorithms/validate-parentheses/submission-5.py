class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {"}":"{", ")":"(", "]":"["}
        stack = []
        for i in s:
            if i in mymap: 
                #if it is a closing parentheses
                if len(stack) == 0: 
                    return False
                elif mymap[i] == stack[-1]: 
                    stack.pop()
                else: 
                    return False
                continue
            else: 
                stack.append(i)
        
        if(len(stack) == 0):
            return True
        return False 