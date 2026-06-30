class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {']':'[', ')':'(', '}':'{'}
        stack = []

        for i in s: 
            if i in mymap: 
                #if it is a key
                if (len(stack) != 0) and stack[-1] == mymap[i]: 
                    #in this scenario pop off the stack
                    
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)

        return not stack 
