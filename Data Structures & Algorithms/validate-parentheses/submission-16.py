class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for i in range(len(s)): 
                
            if s[i] in ['(', '[', '{']:
                curr.append(s[i])
                continue
            else: 
                if not curr:
                    return False
                    
            if i != 0 and s[i] == ')' and curr[-1] == '(': 
                curr.pop()
                continue               
            elif i != 0 and s[i] == ']' and curr[-1] == '[':
                 
                curr.pop()
                continue               

            elif i != 0 and s[i] == '}' and curr[-1] == '{': 
                curr.pop()
                continue               
            else: 
                return False
        

        return len(curr) == 0
            
            
                

