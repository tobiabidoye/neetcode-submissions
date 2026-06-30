class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))] 
        mystack = [] #stores a pair for temperature and index for difference   

        for i, j in enumerate(temperatures):
            while mystack and j > mystack[-1][0]: 
                stackT , stackInd = mystack.pop()
                res[stackInd] = (i - stackInd)
            mystack.append([j, i])

        return res 


        
            
            

