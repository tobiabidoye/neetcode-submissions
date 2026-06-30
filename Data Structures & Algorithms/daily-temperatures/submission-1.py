class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack = []
        output = [0 for i in range(len(temperatures))]

        for i, j in enumerate(temperatures): 
            print(output)
            
            while mystack and j > mystack[-1][0]: 
                temp,index = mystack.pop()
                output[index] = i - index 
            mystack.append([j, i]) 
        
        return output

             

