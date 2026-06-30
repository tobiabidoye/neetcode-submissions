class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i, j in enumerate(temperatures): 
            
            while stack and j > stack[-1][0]: 
                output, index = stack.pop()
                res[index] = i - index
            stack.append([j, i])
        
        return res