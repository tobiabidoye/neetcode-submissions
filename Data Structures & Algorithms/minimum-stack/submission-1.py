class MinStack:

    def __init__(self):
        self.mystack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
       #push into regular stack and min stack at the same time
        self.mystack.append(val)
        if not self.minstack: 
            #inserts initial value
            self.minstack.append(val)
        else: 
            #compares each value to current min which is the top of the minstack
            #if it is the true minimum, then we append it to the top 
            #if not then we append the old min again
            self.minstack.append(min(val,self.minstack[-1])) 


    def pop(self) -> None:
        self.mystack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.mystack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
