class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {')': '(', ']': '[', '}':'{'}
        stack = []     
        for i in s: 
            if i in mymap:
                #if key in map
                #if it starts with closing
                if stack and stack[-1] == mymap[i]:
                    #if element in stack is a matching opening parentheses
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(i)
        
        return not stack


    