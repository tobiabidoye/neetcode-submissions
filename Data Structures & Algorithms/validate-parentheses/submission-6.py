class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {'}':'{', ')':'(', ']':'['}
        stack = []
        for i in s: 

            if i in mymap: 
                if len(stack) != 0 and mymap[i] == stack[-1]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
        
        return not stack