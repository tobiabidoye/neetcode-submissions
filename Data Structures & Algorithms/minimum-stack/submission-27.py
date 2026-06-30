class MinStack:

    def __init__(self):
        self.mystack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.mystack.append(val)

        if not self.minstack: 
            self.minstack.append(val)
            return 

        if self.minstack[-1] > val: 
            self.minstack.append(val)
        else: 
            self.minstack.append(self.minstack[-1])
        

    def pop(self) -> None:
        self.mystack.pop()
        self.minstack.pop()


    def top(self) -> int:
        
        return self.mystack[-1]

    def getMin(self) -> int:
        
        return self.minstack[-1]
