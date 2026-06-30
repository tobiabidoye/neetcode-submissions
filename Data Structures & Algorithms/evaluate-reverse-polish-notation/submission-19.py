class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []

        for i in tokens: 

            if i == '+': 
                mystack.append(mystack.pop() + mystack.pop())
            elif i == '*':  
                mystack.append(mystack.pop() * mystack.pop())
            elif i == '-': 
                x = mystack.pop()
                y = mystack.pop()
                mystack.append(y - x)
            elif i == '/':  
                x = mystack.pop()
                y = mystack.pop()
                mystack.append(int(y / x))
            else: 
                mystack.append(int(i))
        
        return mystack[0]