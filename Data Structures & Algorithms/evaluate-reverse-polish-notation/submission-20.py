class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        

        for i in tokens: 
            print(mystack)
            if i == '+': 
                mystack.append(mystack.pop() + mystack.pop())
            elif i == '*': 
                mystack.append(mystack.pop() * mystack.pop())
            elif i == '-':
                y = mystack.pop()
                z = mystack.pop()
                mystack.append(z - y) 
            elif i == '/':
                y = mystack.pop()
                z = mystack.pop()
                mystack.append(int (z/y)) 
            else: 
                mystack.append(int(i))
        print(mystack)
        return mystack[0]
                
