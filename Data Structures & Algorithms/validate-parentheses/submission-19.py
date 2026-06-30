class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in s: 
            if i in ['(', '{', '[']: 
                res.append(i)
                continue
            elif len(res) == 0: 
                return False 

            if i == ')' and res[-1] == '(': 
                res.pop()
                continue
            elif i == '}' and res[-1] == '{': 
                res.pop()
                continue 
            elif i == ']' and res[-1] == '[': 
                res.pop()
                continue
            else: 
                print(res)
                return False
        print(res)
        return len(res) == 0