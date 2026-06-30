class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens: 

            if i == "+": 
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == "*": 

                stack.append(stack.pop() * stack.pop())
            elif i == "/": 
                #we must always ensure the order of division is the first appearing num divided by the second one
                #so we pop most recent off the stack and least recent off and then divide the least recent by most recent
                a = stack.pop()
                b = stack.pop()
                stack.append(int( float(b) / a))
            else: 
                stack.append(int(i))
        
        return stack[0]
