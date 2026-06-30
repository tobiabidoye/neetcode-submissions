class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []

        for i, j in enumerate(temperatures): 
            while stack and j > stack[-1][0]: 
                value, index = stack.pop()
                res[index] = i - index
            stack.append([j, i])
        
        return res